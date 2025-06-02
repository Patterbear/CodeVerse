For folks who have a Windows background, in Windows, you used to have something called "My Computer", which of late is referred to as "This PC". Inside that, you see various devices like C: (C Drive), D: etc.

ℹ️ Why does it start from C? Ever wondered why there is no A: or B:? 🤔

These were meant for Floppy Drives which are not present in modern day laptops/desktops, so for backward compatibility, this convention has stuck to this day.

https://superuser.com/questions/231273/what-are-the-windows-a-and-b-drives-used-for

Suppose you have a very large hard-disk, say 1TB in size and you would like to manage it as 4 different smaller drives each with about 250GB of disk space. What you can do is to take the disk and divide it into smaller partitions.

(Partition image here)

Once partitioned, you install a filesystem in each of the partitions. Once this is done, it appears as the devices above.

What is the equivalent of this in Linux?

In Linux, we have a philosophy called "Everything is a file". So this 1TB hard-disk appears as a device in the `//dev` directory, so this device may appear as a file like `/dev/sda`.

Now, let's say this device has 4 partitions. Each of these partitions appears as a device file of its own. So these will have names like `/dev/sda1`, `/dev/sda2` and so on.

You now install a filesystem into these partitions and then perform an operation called "mount".

In Linux, we don't have an equivalent of a "My Computer" or "This PC". Rather everything resides under a single directory called `/`. Every single file/directory in your system comes under `/`. There can only be one `/` per running Linux OS. This is referred to as the root filesystem.

https://tldp.org/LDP/sag/html/root-fs.html

Under `/` you have various directories. You can see this using a command `ls /`.

Here are some commonly found directories in the root of your Linux filesystem (i.e. inside `/`):

- `bin`
- `boot`
- `dev`
- `etc`
- `home`
- `lib`
- `media`
- `mnt`
- `proc`
- `root`
- `run`
- `sys`
- `tmp`
- `usr`
- `var`

We sometimes refer to these as the top-level directories. All Linux installations will have almost the same top-level directories.

Each of these directories serve specific purposes.

So when installing Linux, we pick one of our partitions (say `/dev/sda1`) and we ask the installer to install Linux in this partition. So these top-level directories are created in this partition.

Now, all other partitions, `/dev/sda2`, `/dev/sda3` etc are mounted in a location under `/`. The devices are mostly mounted under `/media` (or sometimes in `/mnt`) but it doesn't need to be. You can mount it anywhere under `/`.

This is different from Windows, where the entire Windows is in `C:`, and then there is a `D:` and there is no relationship between `C:` and `D:`. The only thing housing both is "This PC".

Whereas, in Linux, the primary partition from where you have booted Linux, that is where `/` exists and the top-level directories and all other partitions are mounted under `/` somewhere.

This is what you are seeing in the output of the `df -h` command above.

`df -h` tells me the device/partition mounted as `/` (in the sample output above, it is `/dev/sda1`).

There are 2 ways to see these mounted partitions (eg: `/dev/sda5`):

- From the machine's perspective, this is a "device" that allows me to store and retrieve bytes
- From a human's perspective, this is a "partition" into which I can store and retrieve files

So, as a human, when I want to perform filesystem operations like create file, create directory, write some content to a file, delete a directory etc, these operations are performed using filesystem commands like `mkdir`, `touch`, `cat`, `rm` etc and we perform these operations with the mounted view of the partition, i.e., we perform these operations at the location `/media/store1`. So we can create a file, say `foo` in this partition by running these commands:

```
john@neo:~$ cd /media/store1
john@neo:/media/store1$ touch foo
john@neo:/media/store1$ 
```

Now, when I perform these operations, the commands get translated to the corresponding binary operations and the filesystem driver and the device driver work together to perform the actual operation of storing/retrieving the bytes to/from the underlying disk partition. These binary operations are performed with the "device view", i.e. the file `/dev/sda1`.

So, basically, there are 2 views of the same storage device: one is from the perspective of a human (eg: locations like `/media/store1`) and the other is from the perspective of the machine (eg: locations like `/dev/sda1`) and hence the 2 different columns in the `df -h` output.