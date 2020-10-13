# Build the project for selected target

To build Phoenix-RTOS for selected platform you should edit build.project file and set TARGET variable to define target processor architecture and target board.

## Available target platforms






## Running build.sh script

```
	./phoenix-rtos-build/build.sh clean all
```
After the build successfully completes, kernel and disk images will be created and placed in the *_boot* directory.
