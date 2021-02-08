# Graphics library (libgraph)

`libgraph` is a graphics library which allows for scheduling and (possibly hardware accelerated) execution of 2D graphics operations.\
Source code: https://github.com/phoenix-rtos/phoenix-rtos-corelibs/tree/master/libgraph

# Graphics operations
The library supports following graphics operations with 1, 2 and 4-byte color depth:
- drawing lines
![image](_images/line.png)
- drawing rectangles
![image](_images/rect.png)
- filling polygons
![image](_images/fill.png)
- printing text
- copying and moving memory
- changing cursor shape and position

# Graphics adapters
The library supports following graphics adapters:
- virtio-gpu (software emulated graphics under QEMU or VirtualBox),
- AMD Geode LX
- CT69000
- S3 Savage4
