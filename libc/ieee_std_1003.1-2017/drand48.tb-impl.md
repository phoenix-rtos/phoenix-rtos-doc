###Synopsis

`#include <stdlib.h>`

`double drand48(void);`
`double erand48(unsigned short xsubi[3]);`
`long jrand48(unsigned short xsubi[3]);`
`void lcong48(unsigned short param[7]);`
`long lrand48(void);`
`long mrand48(void);`
`long nrand48(unsigned short xsubi[3]);`
`unsigned short *seed48(unsigned short seed16v[3]);`
`void srand48(long seedval); `

###Description

The functions generate uniformly distributed pseudo-random numbers using a linear congruential algorithm and `48`-bit integer arithmetic.

Arguments:
    
<u>xsubi</u> - a work vector used in generating the pseudo-random numbers.

<u>param</u> - parameter values for the `48` bit pseudo-random number generation routines.

<u>seed16v</u> - a `48`-bit number that is used as the seed for pseudo-random number generation. Each element of <u>seed16v</u> contains `16` bits of the number.

<u>seedval</u> - a beginning value for the pseudo-random number sequence. For the same seed the same sequence of numbers is generated.

The initializer function `srand48()` sets the high-order `32` bits of `X`<sub>`i`</sub> to the low-order `32` bits contained in its argument. The low-order `16` bits of `X`<sub>`i`</sub> are set to the arbitrary value `330E`<sub>`16`</sub>.

The initializer function `seed48()` sets the value of `X`<sub>`i`</sub> to the `48`-bit value specified in the argument array. The low-order `16` bits of `X`<sub>`i`</sub> are set to the low-order `16` bits of `seed16v[0]`. The mid-order `16` bits of `X`<sub>`i`</sub> are set to the low-order `16` bits of `seed16v[1]`. The high-order `16` bits of `X`<sub>`i`</sub> are set to the low-order `16` bits of `seed16v[2]`. In addition, the previous value of `X`<sub>`i`</sub> is copied into a `48`-bit internal buffer, used only by `seed48()`, and a pointer to this buffer is the value returned by `seed48()`. This returned pointer, which can just be ignored if not needed, is useful if a program is to be restarted from a given point at some future time-use the pointer to get at and store the last `X`<sub>`i`</sub> value, and then use this value to reinitialize via `seed48()` when the program is restarted.

The initializer function `lcong48()` allows the user to specify the initial `X`<sub>`i`</sub>, the multiplier value `a`, and the added value `c`. Argument array elements:
    
 * `param[0-2]` specify `X`<sub>`i`</sub>, 
 * `param[3-5]` specify the multiplier `a`,
 * `param[6]` specifies the `16`-bit added value `c`. 
    
After `lcong48()` is called, a subsequent call to either `srand48()` or `seed48()` restores the standard multiplier and addend values, `a` and `c`, specified above.

The `drand48()` and `erand48()` functions return non-negative, double-precision, floating-point values, uniformly distributed over the interval `[0.0,1.0)`.

The `lrand48()` and `nrand48()` functions return non-negative, long integers, uniformly distributed over the interval [`0`,`2`<sup>`31`</sup>).

The `mrand48()` and `jrand48()` functions return signed long integers uniformly distributed over the interval [`-2`<sup>`31`</sup>,`2`<sup>`31`</sup>).

The `srand48()`, `seed48()`, and `lcong48()` functions are initialization entry points, one of which should be invoked before either `drand48()`, `lrand48()`, or `mrand48()` is called. (Although it is not recommended practice, constant default initializer values are supplied automatically if `drand48()`, `lrand48()`, or `mrand48()` is called without a prior call to an initialization entry point.) The `erand48()`, `nrand48()`, and `jrand48()` functions do not require an initialization entry point to be called first.

All the routines work by generating a sequence of `48`-bit integer values, X<sub>i</sub>, according to the linear congruential formula:

`X`<sub>`n+1`</sub> = (`aX`<sub>`n`</sub> + `c`)<sub>`mod m`</sub> , where  `n>= 0` 

The parameter `m` = `2`<sup>`48`</sup>; hence `48`-bit integer arithmetic is performed. Unless `lcong48()` is invoked, the multiplier value `a` and the addend value `c` are given by:

`a` = `5DEECE66D`<sub>`16`</sub> = `273673163155`<sub>`8`</sub>

`c` = `B`<sub>`16`</sub> = `13`<sub>`8`</sub> 

The value returned by any of the `drand48()`, `erand48()`, `jrand48()`, `lrand48()`, `mrand48()`, or `nrand48()` functions is computed by first generating the next `48`-bit `X`<sub>`i`</sub> in the sequence. Then the appropriate number of bits, according to the type of data item to be returned, are copied from the high-order (leftmost) bits of `X`<sub>`i`</sub> and transformed into the returned value.

The `drand48()`, `lrand48()` and `mrand48()` functions store the last `48`-bit `X`<sub>`i`</sub> generated in an internal buffer; that is why the application ensures that these are initialized prior to being invoked. The `erand48()`, `nrand48()`, and `jrand48()` functions require the calling program to provide storage for the successive `X`<sub>`i`</sub> values in the array specified as an argument when the functions are invoked. That is why these routines do not have to be initialized; the calling program merely has to place the desired initial value of `X`<sub>`i`</sub> into the array and pass it as an argument. By using different arguments, `erand48()`, `nrand48()`, and `jrand48()` allow separate modules of a large program to generate several independent streams of pseudo-random numbers; that is, the sequence of numbers in each stream does not depend upon how many times the routines are called to generate numbers for the other streams.

The `drand48()`, `lrand48()` and `mrand48()` functions are not thread-safe.

###Return value

As described above.

###Errors

No errors are defined.

###Examples

None.

###Implementation tasks

* Implement `lcong48()`,
* Implement `seed48()`,
* Implement `srand48()`,
* Implement `drand48()`,
* Implement `erand48()`,
* Implement `jrand48()`,
* Implement `lrand48()`,
* Implement `mrand48()`,
* Implement `nrand48()`.
