One very important thing that these distributions provide is a "package management system". A package manager is a set of tools that helps us to install, upgrade, uninstall software packages.

More about package managers here: https://en.wikipedia.org/wiki/Package_manager

In Linux, when we want to install software, most of the times, we don't go to a website, download an installer (like setup.exe), and then go through a wizard to install the software. We rather install software using a package manager in the command line interface.

What are the popular package managers in the Linux distros?

- In RedHat family, we mostly use YUM and RPM.
- In Debian family, we use dpkg and APT.

So in a Debian based distro, when we want to install software, eg: we want to install Firefox, we open a terminal and type a command like:

```bash
sudo apt install firefox
```

If we are using Fedora or RHEL, we can install applications using dnf (or yum). Example:

```bash
sudo dnf install docker
```

Note the use of `sudo`. This is required in a command when we need administrative privileges to run a command. There are 2 options when we need to run a command with administrative privileges:

- Change to root user and then run the command:

```bash
su root
dnf install firefox
```

- If the current user has `sudo` privileges we can prefix the command with `sudo`

```bash
sudo dnf install firefox
```

Don't worry if you don't get this yet. We will clarify about the different users in a subsequent skill.