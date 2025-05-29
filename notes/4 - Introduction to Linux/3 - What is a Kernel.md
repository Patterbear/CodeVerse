We say, the kernel is like the heart of the Operating SYstem. It is the first thing that boots up when you switch on your laptop.

Among the hardware devices mentioned, some are absolute musts for a machine to exist - eg, CPU and RAM are absolutely essential for your Operating System to function. The code related to managing these hardware devices is part of the kernel.

https://simple.wikipedia.org/wiki/Kernel_(computer_science)

The other things like storage, network etc may or may not be part of the kernel depending on how the Operating Systems are written. Microkernel Operating Systems don't have these, while Monolithic kernel based Operating Systems may contain these additional functionalities.

Linux was designed with a monolithic kernel. So many functionalities related to filesystems, networking etc are already part of the kernel, which is why when you install Linux, most of the times, you don't need to "install" any additional drivers. There is a good chance that Linux already recognizes the devices that your laptop contains as well as the ones that you connect to it externally (eg: a tablet, or a pen-drive).