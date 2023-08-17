# Testing process

The testing process uses a Phoenix-RTOS testing framework written in Python. The framework provides an environment for
running both unit and functional tests.
Unit tests are written using [Unity](http://www.throwtheswitch.org/getting-started-with-unity) and the process is
adapted to it.

Tests, in general, are launched using test runner, placed in
[phoenix-rtos-tests](https://github.com/phoenix-rtos/phoenix-rtos-tests) repository.
Read more about the reference project repository [here](../building/project.md).

## High level overview of the test runner

Testing parts of operating systems involves interacting with emulators and physical devices. To simplify this process,
we have developed a framework called the test runner, which automates running tests and facilitates their creation.

Most tests consist of three components:

- An executable binary that is being tested.
- A Python harness that supervises the test execution and interacts with the test.
- A YAML configuration file that connects the harnesses to binaries and contains additional information, such as
the list of target devices on which the test should be run, whether it is a nightly test, or any extra arguments to be
passed to the test harness.

The test runner iterates over the YAML configurations, loads them, and initiates the execution of tests based on
the provided information. A test campaign is run for a specific target device specified by the user. The test runner
performs the following steps:

- Based on the target device, it spawns an emulator process or attempts to connect to a physical device using the
provided serial port.
- If the target device is a physical device, the runner flashes the image (depending on `--no-flash` argument).
- The test campaign is then executed. For each test, the corresponding executable is flashed onto the device
(if needed), the executables are executed, and the harnesses supervise the test execution. If something does not go as
 expected, the runner tries to provide as much information as possible based on the encountered error.
- Finally, the overall test result is printed.

The test runner does not build the project for you. You need to add the test parameter to the build script to ensure
that the tests will be built. If you want to test the `phoenix-rtos-ports`, make sure that the ports are built and
include the `LONG_TEST=y` environment variable during the building process.

Some targets require extra steps to make them compatible with the test runner. For example, the `ia32-generic-qemu`
target must be built with a custom syspage that includes the UART driver. Here is an example command to build an image
with ports for the `ia32-generic-qemu` target:

```bash
TARGET=ia32-generic-qemu CONSOLE=serial LONG_TEST=y ./phoenix-rtos-build/build.sh all test
```

But most of the targets can be build using simple:

```bash
TARGET=target ./phoenix-rtos-build/build.sh core fs project image test.
```

Currently, only user space tests are supported.

## How to write and run tests?

## One time setup

Python packages required by the testing script have to be installed. To do this, create the virtual environment, change
the directory to `phoenix-rtos-tests` and run the following command:

```bash
pip3 install -r requirements.txt
```

## Example 1: Hello world

In this section, we will provide a few basic examples to clarify how to create tests that can be run using the test
runner.

Let's start with the simplest example: a program that prints "Hello, world!" (this example is also included in the
repository in the `sample` directory). We will need four components: a program written in C, a Makefile that builds the
executable, a Python harness to test the program execution, and a YAML configuration file to connect everything
together.

First, let's create the executable to test. Create a directory called `hello` in the `phoenix-rtos-tests/hello`
directory and place the `hello.c` file inside it:

```c
#include <stdio.h>

int main(void)
{
	puts("Hello, world!");
	return 0;
}
```

Now, we need to ensure that it is built within our project. To do that, we define Makefile in the same directory:

```makefile
NAME := hello
LOCAL_SRCS := hello.c

include $(binary.mk)
```

On most targets, programs located in the `phoenix-rtos-tests` directory will be built and included in the filesystem.
We have the first component - the binary that we are going to test.

Next, let's focus on creating the harness that supervises the test. The harness is a program written in Python,
and its main task is to communicate with the test binary and read its output. For this purpose, we will use the
[pexpect library](https://pexpect.readthedocs.io/en/stable/) that is built-in inside the runner. Create a file named
`hello_harness.py` in the `phoenix-rtos-tests/hello` directory and place the following code there:

```python
from trunner.dut import Dut

# The "main" function for test is the harness. Every harness must define a function with this name.
def harness(dut: Dut): # Dut wraps pexpect object, but you should use it as a normal pexpect spawn object.
    expected = "Hello, world!"
    line = dut.readline().rstrip() # Read the line that has been printed by a device.
    assert line == expected, f"Line mismatch! Expected: {expected}, got: {line}" # Assure that the read line is `Hello, world!` message.
```

Notice that you don't have to worry about following:

- How the test is flashed into the board.
- What kind of shell is running inside the device.
- How the test binary should be executed (whether it is a filesystem or a syspage?).

All of these things are handled by the runner. However, it's important to be aware that harnesses are not sandboxes.
For example, if you send a `SIGKILL` signal, you may kill your test binary process and end up in a shell. We also
support the "fast" path of test execution, which means if there is no need to restart the device, we don't do it.
Because of that, if you spawn any new processes on your own or create some resources, you must clean them up.

Now, let's move on to the last step. We have the binary that we want to test, and we have defined the harness that
ensures everything executes correctly. The next step is to define the YAML configuration file that connects them
together.

Define a YAML configuration file called `phoenix-rtos-tests/hello/test_config.yaml`:

```yaml
test:
  tests:
    - name: hello-world
      harness: hello_harness.py
      execute: hello
```

In this configuration, we start with the keyword `test`, which indicates that we are defining the configuration for the
test. Then, we can define the main configuration that will be applied to all tests (which is not included here, but have
it in mind, we will use it in other examples). Next, we define the tests using the `tests` keyword. In this example, the
test consists of a name that the runner will use to print the results, the harness file, and the binary that will be
executed. If we do not define any target, the runner will use the default list of targets on which the test will run.

Important note: Every YAML configuration must start with the `test_` prefix.

Finally, we can verify that everything works correctly. First, let's build the project:

```bash
TARGET=ia32-generic-qemu CONSOLE=serial ./phoenix-rtos-build/build.sh core fs project image test
```

Once the project is built, we are ready to run our test:

```bash
./phoenix-rtos-tests/runner.py --target ia32-generic-qemu -t phoenix-rtos-tests/hello/test_config.yaml
```

We should expect the following output:

```shell
Flashing an image to device...
Done!
phoenix-rtos-tests/hello/hello-world: OK
TESTS: 1 PASSED: 1 FAILED: 0 SKIPPED: 0
```

The output provides information that the device has been flashed correctly (even if it's an emulator process), followed
by the list of tests with their results. At the end, we get a summary of all the tests.

Now, let's go back to the `hello_harness.py` and change the expected message:

```python
# We removed a comma to force a failed assertion.
expected = "Hello world!"
```

Run tests one more time. Now the output should differ from the previous one:

```shell
Flashing an image to device...
Done!
phoenix-rtos-tests/hello/hello-world: FAIL
ASSERTION TRACEBACK (most recent call last):
  File "/home/user/phoenix-rtos-project/phoenix-rtos-tests/hello/hello_harness.py", line 7, in harness
    assert line == expected, f"Line mismatch! Expected: {expected}, got: {line}" # Assure that the read line is `Hello, world!` message.

ASSERTION MESSAGE:
Line mismatch! Expected: Hello world!, got: Hello, world!
TESTS: 1 PASSED: 0 FAILED: 1 SKIPPED: 0
```

As we can see, the test finished with a failure. As a result, the runner printed more information, including a trace
back and an assertion message. Depending on the exception type, the runner will try to provide as much information as
possible.

## Example 2: unit tests using C

In this section, we will explore another type of test: unit testing. When we talk about testing, unit testing often
comes to mind, which is why the test runner has native support for unit testing. Similar to the previous section,
we start by creating a C file named `dummy.c` located in the `phoenix-rtos-tests/dummy` directory. To write unit tests,
we will use the modified [Unity Test](http://www.throwtheswitch.org/unity), a third party unit testing framework
built for C.

```c
#include <string.h>

#include "unity_fixture.h"

TEST_GROUP(dummy);

TEST_SETUP(dummy)
{
}

TEST_TEAR_DOWN(dummy)
{
}

TEST(dummy, memset)
{
	unsigned char buffer[2] = {0, 0};
	memset(buffer, 0xFF, 2);
	for (int i = 0; i < 2; i++) {
		TEST_ASSERT_EQUAL_CHAR(buffer[i], 0xFF);
	}
}

TEST(dummy, strlen)
{
	const char *s = "Dummy string";
	TEST_ASSERT_EQUAL(strlen(s), 12);
}

TEST(dummy, ok)
{
	TEST_PASS_MESSAGE("dummy test that always pass");
}

TEST_GROUP_RUNNER(dummy)
{
	RUN_TEST_CASE(dummy, memset);
	RUN_TEST_CASE(dummy, strlen);
	RUN_TEST_CASE(dummy, ok);
}

void runner(void)
{
	RUN_TEST_GROUP(dummy);
}

int main(int argc, char *argv[])
{
	UnityMain(argc, (const char**)argv, runner);
	return 0;
}
```

This test runs the test group called `dummy`, which consists of three tests: `memset`, `strlen`, and `ok`. If you want
to learn more about what unity framework offers, you can visit their
[GitHub website](https://github.com/ThrowTheSwitch/Unity).

As in the previous example, we need to have the executable binary as a result, so let's create the following `Makefile`
in the same location:

```makefile
NAME := test-dummy
LOCAL_SRCS := dummy.c
DEP_LIBS := unity

include $(binary.mk)
```

The last step is to create the YAML configuration for the test. In the same location, create the YAML configuration
file called `test_dummy.yaml`:

```YAML
test:
  tests:
    - name: test-dummy
      type: unity
      execute: test-dummy
```

The configuration above is similar to the configuration we defined in the previous section. The main difference is lack
of keyword `harness`, and instead, we use the keyword `type` with the string `unity` as value. This line instructs the
runner to use internally defined harness to parse the output. Therefore, the runner works in the same manner, but
instead defining the harness ourselves, we have ready-to-use harness that will be used when `type: unity` is specified.

Now, you can run the tests and expect the success:

```shell
./phoenix-rtos-tests/runner.py --target ia32-generic-qemu -t phoenix-rtos-tests/dummy/test_dummy.yaml
Flashing an image to device...
Done!
phoenix-rtos-tests/dummy/test-dummy: OK
TESTS: 1 PASSED: 1 FAILED: 0 SKIPPED: 0
```

To see more information, add the `--verbose` flag:

```shell
./phoenix-rtos-tests/runner.py --target ia32-generic-qemu -t phoenix-rtos-tests/dummy/test_dummy.yaml --verbose
Flashing an image to device...
Done!
phoenix-rtos-tests/dummy/test-dummy: OK
	TEST(dummy, memset) OK
	TEST(dummy, strlen) OK
	TEST(dummy, ok) OK
TESTS: 1 PASSED: 1 FAILED: 0 SKIPPED: 0
```

Finally, we can force runner to fail to see how the output will look like. Change the line in the dummy `ok` test to
`TEST_FAIL_MESSAGE("dummy test that always pass");`. Rebuild the project and run tests one more time:

```shell
/phoenix-rtos-tests/runner.py --target ia32-generic-qemu -t phoenix-rtos-tests/dummy/test_dummy.yaml
Flashing an image to device...
Done!
phoenix-rtos-tests/dummy/test-dummy: FAIL
	TEST(dummy, ok) FAIL at phoenix-rtos-tests/dummy/dummy.c:27: dummy test that always pass
TESTS: 1 PASSED: 0 FAILED: 1 SKIPPED: 0
```

As we can see, the runner caught failed test and provided information about the failure.

## Example 3: more advanced test case

In this example, we will demonstrate what we can achieve using additional features of the runner and its YAML
configurations. Without surprise, we create a new C program in the same location, which is the
`phoenix-rtos-tests/hello` directory. Let's name this file `hello_arg.c` and put the following content inside it:

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
	char word[10];

	if (argc <= 1) {
		puts("One argument is required! You passed zero.");
		return 1;
	}

	if (argc > 2) {
		puts("One argument is required! You passed more than one.");
		return 2;
	}

	printf("Hello, %s!\n", argv[1]);

	fgets(word, 10, stdin);
	printf("%s", word);

	return 0;
}
```

This program checks the number of arguments. If there is exactly one argument, it continues its execution; otherwise,
the program ends with a message describing how many arguments must be passed. After that, it prints the argument that
was passed within the greeting sentence. Finally, it reads input (up to 9 characters) from stdin and prints it out.
Thus, we can pass arguments and provide the input to the test.

Of course, we need to add some lines to the Makefile:

```makefile
NAME := test-hello-arg
LOCAL_SRCS := hello_arg.c

include $(binary.mk)
```

Now, let's create `hello_arg_harness.py` in the same directory with the following content:

```python
from trunner.dut import Dut

def harness(dut: Dut, **kwargs):
    argc = kwargs.get("argc", 1)
    input = kwargs.get("input", "Bye!")

    assert argc >= 0

    if argc < 1:
        dut.expect_exact("One argument is required! You passed zero.")
        return
    elif argc > 1:
        dut.expect_exact("One argument is required! You passed more than one.")
        return

    dut.expect(r"Hello, \w+!\r*\n")
    dut.sendline(input)
    dut.expect(rf"{input}\r*\n")

    if len(input) > 10:
        output = input[:9]
    else:
        output = input + r"\r*\n"

    dut.expect(output)
```

This harness differs from the previous one in the definition of the `harness` function. Instead of using only `dut` as
an argument, we have added **kwargs in the definition. Using kwargs, we can pass user-defined input to the test by
adding a `kwargs` dictionary to the YAML configuration or by passing them to the runner using the `--kwargs` argument.
We will describe this in more detail later.

In the `harness` function, we read the arguments, ensuring they have default values if they are not passed. Then we
perform different actions based on the `argc` argument. If `argc` differs from 1, we expect the error messages and
finish the harness execution. If there is exactly one argument, we expect the greeting sentence and send the input that
should be printed back to us.

Now, let's create some test cases based on our harness using the YAML configuration file:

```yaml
test:

  targets:
    value: [ia32-generic-qemu, armv7a9-zynq7000-qemu, host-generic-pc]

  nightly: true

  tests:
    - name: arg_zero
      execute: test-hello-arg
      harness: hello_arg_harness.py
      kwargs:
        argc: 0
      targets:
        exclude: [armv7a9-zynq7000-qemu]

    - name: arg_two
      execute: test-hello-arg arg1 arg2
      harness: hello_arg_harness.py
      kwargs:
        argc: 2
      targets:
        value: [ia32-generic-qemu]

    - name: arg_hello
      execute: test-hello-arg world
      harness: hello_arg_harness.py
      nightly: false
      kwargs:
        input: 'Adios!'

    - name: arg_hello_too_long_input
      execute: test-hello-arg space
      harness: hello_arg_harness.py
      kwargs:
        input: 'String that is too long!'
```

This time, the configuration is a bit longer and requires more explanation. Let's start from the beginning. Before the
keyword `tests`, we defined `targets`, which is a dictionary with allowed keys: `value`, `include` and `exclude`. As we
mentioned in the previous sections, tests are allowed to run on a list of default targets. If we want to change the
targets by defining a strict list of targets or including/excluding them, we can do exactly that by defining a `targets`
dictionary.

As you can see, `targets` is used in the `test` scope. We call this scope the main config. The set of keywords that you
can use in the main config is a subset of the keywords allowed to be used in a single test configuration (elements of
the `tests` list). These keywords are: `targets`, `type`, `nightly`, `ignore`. If these keywords are not defined in the
single test configuration, then they will be taken from the main configuration (if present). However, targets are joined
by a special rule.

If `targets` with the key `value` is defined in the single test configuration, the targets from the main configuration
is not considered. If the `targets` are used with `exclude` or `include` keyword, the test takes the value from the main
config (or the default targets if there is no main config) and applies `include`/`exclude` operation on that set.

In this example, we specify that this test campaign is allowed to run only on three targets: `ia32-generic-qemu`,
`armv7a9-zynq7000-qemu`, and `host-generic-pc`. We also set the `nightly` option to true, which means the tests will
only be run if the `--nightly` flag is passed as an argument to the runner.

Now let's go through the tests and try to understand the final configuration:

- The `arg_zero` test specifies that the `test-hello-arg` executable should be executed without any arguments
(`execute: test-hello-arg`). We provide the `hello_arg_harness.py` as the harness. In the `kwargs` section, we set
`argc` to `0`. This dictionary is passed later to the harness as `kwargs` parameter. Additionally, we exclude the
`armv7a9-zynq7000-qemu` target for this specific test. As a result, it will be run on the `ia32-generic-qemu` and
`host-generic-pc` targets.
- The `arg_two` test specifies that the `test-hello-arg` should be executed with two arguments: `arg1` and `arg2`
(`execute: test-hello-arg arg1 arg2`). We provide the `hello_arg_harness.py` as the harness. In the `kwargs` section, we
set `argc` to `2`. Additionally, we specify that this test should only run on the `ia32-generic-qemu` target.
- The `arg_hello` test specifies that the `test-hello-arg` executable should be executed with the argument `world`. We
provide the `hello_arg_harness.py` as the harness. In the `kwargs` section, we set `input` to `Adios!`. This word will
be used as the input to the `test-hello-arg`. We also set `nightly` to false for this specific test. Thanks to that, the
test can be launched always, no matter if `--nightly` is provided.
- The last one, `arg_hello_too_long_input`, is similar to the previous one, but we set `input` to `String that is too
long!`.

These test cases demonstrate different scenarios of executing the `teset-hello-arg` program with different arguments and
inputs and validate the expected behavior using `hello_arg_harness.py` harness.

Now, let's check how the runner will handle this test configuration based on the arguments provided by the user. Let's
start with following command:

```shell
./phoenix-rtos-tests/runner.py -T ia32-generic-qemu -t phoenix-rtos-tests/hello/test_hello_arg.yaml
```

The result should be as follows:

```shell
Flashing an image to device...
Done!
phoenix-rtos-tests/hello/arg_two: OK
TESTS: 1 PASSED: 1 FAILED: 0 SKIPPED: 0
```

The result is expected because there is only one test that does not run in nightly mode and is allowed to run on the
`ia32-generic-qemu` target.

Add the `--nightly` flag to the previous command and compare the output:

```shell
./phoenix-rtos-tests/runner.py -T ia32-generic-qemu -t phoenix-rtos-tests/hello/test_hello_arg.yaml --nightly
Flashing an image to device...
Done!
phoenix-rtos-tests/hello/arg_zero: OK
phoenix-rtos-tests/hello/arg_two: OK
phoenix-rtos-tests/hello/arg_hello: OK
phoenix-rtos-tests/hello/arg_hello_too_long_input: OK
TESTS: 4 PASSED: 4 FAILED: 0 SKIPPED: 0
```

As you can see, all tests were run, and additional, it took more time to execute these tests. In nightly mode, the
runner reboots the device after each test.

We can change the target to verify what `targets` keyword looks like. Change `ia32-generic-qemu` to
`armv7a9-zynq7000-qemu` in the previous command:

```shell
./phoenix-rtos-tests/runner.py -T armv7a9-zynq7000-qemu -t phoenix-rtos-tests/hello/test_hello_arg.yaml --nightly
Flashing an image to device...
Done!
phoenix-rtos-tests/hello/arg_hello: OK
phoenix-rtos-tests/hello/arg_hello_too_long_input: OK
TESTS: 2 PASSED: 2 FAILED: 0 SKIPPED: 0
```

As we could expect, the `arg_zero` wasn't launched because the `armv7a9-zynq7000-qemu` target is excluded in this test
case. The `arg_two` test is also omitted because it can only be run on the `ia32-generic-qemu` target.

If you try to run this test case on a different target not listed in this YAML configuration, the test runner
will finish its execution without executing any test:

```shell
./phoenix-rtos-tests/runner.py -T riscv64-generic-qemu -t phoenix-rtos-tests/hello/test_hello_arg.yaml --nightly
Flashing an image to device...
Done!
TESTS: 0 PASSED: 0 FAILED: 0 SKIPPED: 0
```

## See also

1. [Table of Contents](../README.md)
