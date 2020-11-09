# Introduction to Phoenix-RTOS

The idea for writing a new real-time operating system was born in 1998 at the Warsaw University of Technology. It was the time of the GNU/Linux system, in the era of PCs, when most software engineers were excited about the potential of open source operating systems. The initial motivation was to gain insight into the operating system by implementing it from scratch. Once the prototype was developed, it became clear that a new efficient microkernel suitable for resource constrained devices could be implemented based on the state-of-the-art operating system.

Ten years on, the embedded systems market has grown exponentially, and a new operating system with efficient implementation and rich functionalities is highly required. Most vendors of the Internet of Things devices (e.g. electricity meters) understand that effective software implementation depends on the operating system. From the perspective of a software developer and an architect of embedded systems for the Internet of Things (IoT), the convergence of the application interface of the operating system for the IoT and the general purpose system significantly improves and simplifies the speed of implementation. It also enables software developers with little experience in developing low level software to develop solutions.

## Version 2

Developed until 2013, the Phoenix-RTOS version 2 has been widely implemented in data concentrators for the smart grid, smart energy meters, and smart gas meters, etc. The second version of the system is recognised on the market as a real-time system for the smart grid and software-defined solutions. One of the system modules, Phoenix-PRIME, is the world's first software-defined implementation of the PRIME 1.3.6 PLC standard. The system's biggest advantage is the UN*X application interface, which allows for a wide range of uses in open source applications.

The system’s large, monolithic kernel that implements most of the system functionalities is considered the main limitation of the second version of the system, as its consequences include restricted scalability, modularity, testing possibilities, and increased hardware requirements). The system cannot be easily used in microcontroller-based devices and low power consumption devices.

## Version 3

The decision to develop a new version of the system was made in response to market needs and the trends in the development of microcontrollers. Also, software-defined approach to device development has gained popularity and a number of partners are already using the system in their devices.

## A brief history of operating systems

The operating system history is very long and full of exciting discoveries. Contrary to the popular belief, it is not limited to MS Windows and GNU/Linux. And it is not true that MS Windows 95 was a revolutionary operating system, which changed the world of personal computing.

This table presents a timeline of the most important events in the history of operating systems.

| Date| Operating system | Comment |
--------|---------------------|------------|
| 1962 | CTSS | The first time-sharing operating system |
| 1966 | MULTICS, IBM OS/360 | The first multi-user and multitasking operating systems |
| 1974 | <span style="color:blue">UNIX</span> | <span style="color:blue">The first portable multitasking and multi-user operating system written in high-level language (B and finally C)</span> |
| 1976 | <span style="color:green">RIG</span> | <span style="color:green">The first operating system based on message passing</span> |
| 1977 | <span style="color:violet">CP/M</span> | <span style="color:violet">The first operating system for personal computers</span> |
| 1978 | VMS | The first multitasking and multi-user operating system with a virtual memory (for VAX-11) |
| 1979 | <span style="color:blue">UNIX3 BSD</span> | <span style="color:blue">UN*X operating system with a virtual memory (for VAX-11) </span> |
| 1980 | <span style="color:red">OS-9</span> | <span style="color:red">The first operating system for embedded applications</red> |
| 1981 | Xerox Star | The first operating system with GUI |
| 1981 | <span style="color:violet">MS-DOS</span> | <span style="color:violet">The first operating system for IBM PC</span> |
| 1981 | <span style="color:green">Accent</span> | <span style="color:green">Next-generation operating system based on message passing</span> |
| 1981 | Amoeba | The first distributed operating system |
| 1982 | <span style="color:red">pSOS </span> | <span style="color:red">The popular real-time operating system for embedded systems based on M68000 family </span> |
| 1982 | <span style="color:red">QNX</span> | <span style="color:red">The first real-time operating system based on the UN*X philosophy (Intel 8088)</span> |
| 1983 | GNU/HURD | The first open source operating system (based on a microkernel) |
| 1984 | <span style="color:violet">Mac OS</span> | <span style="color:violet">The first operating system for personal computers with GUI</span> |
| 1984 | <span style="color:blue">SunOS</span> | <span style="color:blue">UN*X developed by Sun Microsystems for SUN computers based on BSD</span> |
| 1985 | AmigaOS | Operating system for Amiga personal computers |
| 1985 | <span style="color:violet">MS Windows 1.01</span> | <span style="color:violet">Graphical environment for MS-DOS</span> | 
| 1986 | <span style="color:green">Mach</span> | <span style="color:green">The first multi-server UN*X emulation based on message passing (for VAX-11)</span> |
| 1987 | <span style="color:blue">Xenix</span> | <span style="color:blue">The UN*X operating system developed by SCO (initially with Microsoft) for IBM PC – the first 32-bit operating system for IBM PC</span> |
| 1987 | <span style="color:red">VxWorks</span> | <span style="color:red">Real-time operating system for safety critical embedded applications</span> |
| 1988 | <span style="color:violet">OS/2</span> | <span style="color:violet">The first operating system with GUI for IBM PC</span> |
| 1990 | <span style="color:violet">MS Windows 3.0</span> | <span style="color:violet">The next generation of graphical environment for MS-DOS with a virtual memory, multiprogramming and MS-DOS virtual machines</span> |
| 1990 | <span style="color:red">QNX4</span> | <span style="color:red">POSIX-compliant real-time operating system with a virtual memory and resource protection</span>|
| 1991 | <span style="color:blue">GNU/Linux</span> | <span style="color:blue">The first open source UN*X operating system based on GNU applications and a monolithic kernel written by Linus Torvalds and other enthusiasts cooperating via the Internet</span> |
| 1991 | GNU/HURD on Mach | The next generation of GNU/HURD based on Mach microkernel |
| 1992 | <span style="color:blue">Solaris</span> | <span style="color:blue">UN*X developed by Sun Microsystems based on SVR4 (a joint project of Bell Labs and Sun Microsystems integrating the best ideas from SVR3, BSD, Xenix and SunOS)</span> |
| 1993 | Plan 9 | A distributed UN*X operating system from Bell Labs |
| 1993 | <span style="color:violet">MS Windows NT</span> | <span style="color:violet">Multitasking and multi-user operating system with an embedded Windows graphical environment based on a new kernel (not on MS-DOS)</span> |
| 1993 | <span style="color:blue">FreeBSD, NetBSD</span> | <span style="color:blue">Open source UN*X operating systems based on BSD |
| 1995 | <span style="color:blue">OpenBSD</span> |  <span style="color:blue">UN*X operating system based on BSD with enhanced cryptography (OpenSSL) and security</span> |
| 1995 | <span style="color:violet">Windows 95</span> | <span style="color:violet">Multitasking 32-bit operating system for IBM PC based on MS-DOS and parts of MS Windows NT</span>
| 1996 | <span style="color:violet">Mac OS X</span> | <span style="color:violet">Multitasking and multi-user operating system from Apple based on Mach microkernel and parts of BSD (XNU)</span>|
| 1996 | <span style="color:red">RTLinux</span> | <span style="color:red">Operating system with GNU/Linux API based on two (Linux and RT) kernels intended for real-time applications</span> |
| 1996 | <span style="color:red">Windows CE</span> | <span style="color:red">Operating system with Windows API for handheld devices and embedded applications</span> |
| 2000 | <span style="color:violet">MS Windows 2000</span> | <span style="color:violet">Next generation of Windows NT</span>|
| 2001 | <span style="color:red">QNX6</span> | <span style="color:red">Microkernel-based POSIX-compliant real-time operating system with a virtual memory and resource protection</span>|
| 2001 | <span style="color:violet">MS Windows Xp</span> | <span style="color:violet">The next generation of MS Windows 2000 integrating MS Windows 9x and MS Windows NT lines</span> |
| 2001 | MAFALDA | Microkernel Assessment by Fault-injection AnaLysis for Design Aid – a series of prototype tools for the assessment of real-time COTS microkernel based systems |
| 2001 | <span style="color:red">Phoenix</span> | <span style="color:red">Operating system prototype developed at the Warsaw University of Technology</span> |
| 2005 | <span style="color:red">Phoenix-RTOS 2</span> | <span style="color:red">Real-time operating system for embedded applications developed as the successor of the Phoenix prototype</span> |
| 2006 | <span style="color:red">FreeRTOS</span> | <span style="color:red">Simple operating system for microcontrollers for embedded applications with a small code footprint</span> |
| 2008 | <span style="color:violet">iOS</span> | <span style="color:violet">Mobile operating system for phones and tablets based on MacOS X</span> |
| 2009 | <span style="color:violet">Android</span> | <span style="color:violet">Mobile operating system for phones and tablets based on GNU/Linux</span> |
| 2010 | <span style="color:violet">Windows Mobile</span> | <span style="color:violet">Mobile operating system for phones and tablets based on Windows Kernel</span> |
| 2017 | <span style="color:red">Phoenix-RTOS 3</span> | <span style="color:red">Real-time operating system for the Internet of Things based on a microkernel with a small code footprint, a virtual memory support, resource protection and numerous application interfaces (native, POSIX, ARINC653)</span> |

The different colours used in the table identify the various operating system types developed over the years.

### MULTICS

The history of MULTICS (Multiplexed Information and Computing Service) began with the CTSS operating system developed at MIT. This system was based around the idea of sharing the CPU among a number of concurrently running programs, which means that one computer could be used by multiple users running multiple tasks. The CTSS system was continued as the Multics project with the aim to create the multiuser and multitasking operating system. At the same time, IBM researched the same area to develop the OS/360 operating system for its IBM S/360 machine.

### <span style="color:blue">UNIX</span>
Bell Laboratories (AT&T) team involved in the MULTICS project was not satisfied with its results, and they decided to leave it. In their opinion, the system was too complicated and too heavily dependent on hardware. As a result, the system was non-portable and demanded a huge development effort. The team decided to write an operating system using a high level language and ensure that it can be implemented universally on different computer platforms. This was the most revolutionary milestone in the history of operating systems, leading to the creation of the most popular operating system UNIX.

The UNIX marks the beginning of a new era in the development of operating systems as well as a departure from the old principle of system-level programming, which could only be done in an assembler. The source code was licensed to numerous companies and universities. One of them, the University of Berkeley, started their own research on operating systems and created their own version of UNIX called BSD (Berkeley Software Distribution).

### <span style="color:green">Microkernel architecture</green>

In 1979, a team from Rochester University presented a framework for a distributed computing environment, which consisted of three large computers (IBM 360, DEC KL10, and CERF) and a gateway minicomputer (Data General Eclipse) connected to terminals, the ARPANET network and local PALO minicomputers over the fast Ethernet. The minicomputer chosen as a gateway processor was controlled by the Aleph operating system based on message passing. This operating system was a precursor to the new operating system architecture called microkernel architecture. In this architecture, the operating system kernel is considerably reduced and is responsible only for basic functions like memory management, process management, simple I/O operations and inter-process communication using message passing. Device drivers are partially or completely moved to the user level and are implemented as regular processes handling I/O messages from other parts of the system. The message passing restricts interactions between system modules to a well-structured format that discourages poorly defined dependencies between processes. This approach dramatically increases system scalability. Operating system modules may interact with modules located on remote computers in the same way as with local modules. All system modules are implemented as user level servers providing a set of services for other modules and can be easily removed or added as needed by a given system, allowing for high configurability and modularity.

The Accent operating system, developed at CMU, was the successor of the Aleph (RIG) project. Accent stands out as a relatively pure example of a communication-oriented operating system, i.e. an operating system which uses the abstraction of communication between processes as its basic organising principle. The integration of a virtual memory support, file access and inter-process communication in Accent contribute to improved performance when compared to previous communication-oriented systems (e.g. [1]) as well as a more ‘transparent’ network operating system design.

### <span style="color:violet">Operating systems for personal computers</span>

In 1974, while working for Intel Corporation Dr. Gary A. Kildall created CP/M as the first operating system for the new microprocessor. By 1977, CP/M had become the most popular operating system in the fledgling microcomputer (PC) industry. The largest Digital Research licensee of CP/M was a small company, which had started life as Traf-0-Data, and is now known as Microsoft.

### <span style="color:red">Realtime operating systems</span>

## Evolution problem

The main problems connected with developing an operating system stem from its structure and evolution. These two factors have a dramatic impact on the overall system stability and code effectiveness. The analysis of the source code of the common open source general-purpose operating systems based on a monolithic kernel clearly shows that the code cannot be properly controlled due to multiple files, macros, and add-ons as well as authors promoting their coding philosophy and coding style.

The main disadvantages of monolithic kernels are the dependencies between system components: when a mechanism becomes obsolete, it cannot be easily removed from the kernel, because the functionality of the other components, e.g. device drivers, depends on the mechanism.

## Less is more

Nowadays, with the explosion of the Internet, the development paradigm is considerably different from the initial ideas developed in the 1970s when UN*X was born. This is due to a significantly lower cost of processing power and the development of managed environments which make it possible to write software without the basic knowledge of computer system architecture. A lot of programmers have stopped solving problems, and instead, they copy-paste the code they find online without a basic understanding of the algorithms. They pay no attention to the amount of consumed memory and processing power. There is a strong push to create new products and bring them quickly to the market with little or no attention paid to their optimised design and system components.

For us, engineering is a form of art, but there are few who share this view. Engineering has transformed into pop-engineering and become a source of revenue for investors and people who ignore technical details and technical beauty.

Fortunately, the embedded system engineering, based on microcontrollers with limited resources, has remained the last bastion of software engineering where less means more. Less code means a more efficient code, fewer hardware components mean a more reliable device, and fewer processing power requirements mean more time spent on batteries.

“Less is more” is a perfect description of good engineering practice, and it should be widely promoted.

## Era of microcontrollers

The analysis of trends in microcontroller evolution related to their growing computing power and a growing size of the available RAM shows that an oversimplification of the architecture of the operating systems for the IoT is not justified. The trends also show that such systems should not be deprived of general use functionalities such as multicore support, threads, processes, a virtual memory based on memory objects, process separation and resource protection, and modern mechanisms for inter-processor synchronization.

Drawing on decades of technological advancements in the field of operating systems, it is possible to create a fully-featured, effective microkernel which allows for the development of both simple applications with no need to use UN*X interface and complex systems which use popular open source components. The kernel size must not exceed 20,000 of code lines. For several years, the idea of creating such a system from scratch has been supported by prominent researchers working in the field of operating systems, including the author of MINIX system A. S. Tanenbaum. An additional advantage of such an effectively implemented system is its reliability and potential for comprehensive tests and audit of the static source code. A well-developed operating system like this is of particular importance for critical applications thanks to a shorter certification process (e.g. acquiring the DO-178C certificate). 

## See also

1. [Table of Contents](README.md)
2. [Phoenix-RTOS architecture](architecture.md)
3. [Building Phoenix-RTOS](building/README.md)
4. [Running Phoenix-RTOS on targets](quickstart/README.md)
