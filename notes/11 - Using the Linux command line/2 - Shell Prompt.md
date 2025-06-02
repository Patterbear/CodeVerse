A shell prompt (or sometimes called the command prompt) is where you type your commands. It is an indication that the system is ready to accept commands from you.

This is what a prompt looks like:

```
john@neo:~$  
```

- The prompt usually tells you what user you are logged in as, followed by a hostname - in simple terms, the name that the machine is referred by. In the above example, `john` is the username and `neo` is the hostname.
- After this comes a `:` followed by something called a "current working directory".
- In the above example, `~` is the current working directory. `~` is a short-cut to mean Home directory of the current user.
- Many commands are contextual and run in the current working directory by default. For eg, the command `ls` prints the contents of the current working directory if there are no arguments after `ls`.
- After the directory, you see a `$` symbol followed by a cursor `█` beeping. That is where you type your commands.

In general, you will see it as:

```
username@hostname:directory$
```

You can also get these details via commands:

- `whoami` - username of the current logged in person
- `hostname` - the hostname of the system
- `pwd` - the current working directory (`~` is same as `/home/<username>`)

When logged in as a root user, you may see a prompt like this:

```
root@neo:~#  
```

Note the use of a `#` symbol instead of `$`.