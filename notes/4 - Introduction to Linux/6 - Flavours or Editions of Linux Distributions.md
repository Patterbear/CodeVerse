Within each distro, we have what are called "flavours" or "editions". For eg, you may find something called a Desktop edition or a Server edition.

Not all Linux installations come with a Graphical User Interface (GUI). The GUI is part of specific flavours of Linux, which are usually referred to as Desktop editions. When you are using Linux in a server, or in the cloud, the operations folks are used to working with such installations without a GUI. These are a different flavour called Server editions.

Linux Distributions timeline: https://upload.wikimedia.org/wikipedia/commons/8/83/Linux_Distribution_Timeline_27_02_21.svg

Both Desktop and Server editions have the Linux kernel and the GNU tools. But Server editions don't have a GUI and are usually lighter on resource consumption (especially RAM).

Cloud providers provide you machines with only 512MB of RAM. You may wonder, what can you do with just 512MB of RAM?! Having a light-weight server edition helps because the OS consumes lesser RAM and leaves more for your applications to run. IOT devices may come with even lesser RAM!

How do you interact with an Operating System that does not come with a GUI? You connect to it using a protocol called SSH and then you can open a shell and invoke commands. We can call such interfaces as Command Line Interfaces (CLI) or sometimes also as Terminal/Text based interfaces. The command line has several commands (like the Coreutils commands mentioned above), related to browsing filesystems, opening, viewing, manipulating and editing files. There are powerful text-based editors like Vim, Emacs etc.

Desktop editions are easier for beginners, but CLIs can be more powerful once you know your way around.

Let us look at some popular distros and the editions they have:

- Ubuntu has the following popular editions (https://ubuntu.com/download)
- Ubuntu Desktop
- Ubuntu Server
- Fedora has the following editions (https://getfedora.org/):
- Fedora Workstation (their Desktop flavour)
- Fedora Server

The server editions are usually lighter when compared to the desktop editions. Distros may also have other editions (like IOT editions).

### Which distributions exist?

There are hundreds of distributions! Here is an [image capturing them](https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg).

### Window Managers in Linux

To understand Desktop Editions, we need to first understand the role of Window Managers.

A Window Manager is a piece of software that controls the appearance and placement of windows in a Graphical User Interface.

The browser window where you are reading this right now is an example of a Window.

Unlike Operating Systems like Windows and Mac, you can choose among several Window Managers based on your needs.

### Types of Window Managers

There are multiple categories of Window Managers:

- Stacking Window Managers
- Tiling Window Managers
- Compositing Window Managers

### Examples of Window Managers

[Mutter](https://en.wikipedia.org/wiki/Mutter_\(software\)), [Compiz](https://en.wikipedia.org/wiki/Compiz) are examples of Window Managers.

### Desktop Environments

Window Managers along with some basic functionality like File system viewers and other applications forms a Desktop Environment. Gnome, KDE, Unity are some popular Desktop Environments.