Ok, we have booted our system. What next?

One of the first things you may want to do when you get a machine is to find out what resources the machine comes with, how many CPUs does it have, the amount of memory (RAM) that it has, the size of the disk, etc.

We will learn a few commands about making sense of the various devices in our machine. Don't try to understand everything in the output.

### CPU

You can get information about your processor using the command: `lscpu`. This command can tell you the type of processor you have, the number of CPU cores you have, the CPU architecture, the speed of your CPU etc. You can also run the command: `cat /proc/cpuinfo` to get similar information.

### RAM

You can use the command `free -m` to find out the total RAM available, the amount used and the amount available. We can also see if swap is enabled, and the amount of swap space available.

What is Swap memory?

In simple terms, swap memory is some space from your storage device (hard-disk or solid state drive) being used like a RAM. Storage devices are order of magnitude slower than RAM so this is not desirable. However when you have run out of memory, the OS will start killing process. So using the storage device like a RAM is perhaps better than allowing the OS to kill processes. If your swap is being consumed often, then it is time to upgrade your system and get a larger RAM! To run user facing applications where performance is important swap memory should be disabled.

Another way to get information about the RAM is using `cat /proc/meminfo`.

### Storage Devices

You can get an idea about the various mounted storage devices, the amount of disk space consumed, disk space available etc using the command `df -h`. Look at the Size, Used, Avail columns.

Sample `df -h` output:

```
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            7.7G     0  7.7G   0% /dev
tmpfs           1.6G  2.3M  1.6G   1% /run
/dev/sda1        94G   80G  9.6G  90% /
/dev/sda5        63G   26G   34G  43% /media/store1
/dev/sda6        94G   79G   11G  88% /media/store2
/dev/sda7        94G   29G   61G  33% /media/store3
/dev/sda8        94G   60G   29G  68% /media/store4
```

What is the above output telling us?

In order to understand this output further, we have to first understand a bit about the Filesystem hierarchy in Linux. Check the section on "An Introduction to the Linux Filesystem Hierarchy" below.

### Network related information

If you want to know the various network interfaces in your system, you can run the command: `ip addr show`.

Sample output:

```
$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp9s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether ab:cd:ef:01:02:03 brd ff:ff:ff:ff:ff:ff
3: wlp8s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1492 qdisc noqueue state UP group default qlen 1000
    link/ether ac:bc:dc:02:03:04 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.110/24 brd 192.168.1.255 scope global dynamic noprefixroute wlp8s0
       valid_lft 255122sec preferred_lft 255122sec
    inet6 fe80::7868:597e:51e:1b2/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

`lo` is called the Loopback interface and is used many a times when testing client-server applications. Interfaces that start with `eth` or `en` mostly represent Ethernet interfaces and the ones that start with `wlan` or `wl` are the Wireless interfaces.

One important thing in the output above, is the value after `inet` and that represents your IP address. The IP address is some kind of a machine identifier and is something we need very often when working with distributed system. A machine can have multiple IP addresses. So in the above example, one of the IP addresses of the machine is `127.0.0.1` and another is `192.168.1.110`.