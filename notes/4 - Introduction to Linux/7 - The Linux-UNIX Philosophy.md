When you start learning the Linux command-line environment, one thing may surprise you. There are commands for seemingly trivial things. For eg, there is a command to print the last few lines of a file (`tail`). And then a separate command to print the first few (`head`).

It is easy to learn these commands and what they do, but like many, I struggled to understand "why" they existed. Why would someone design a command just to get the first few lines of a file? And then a completely different command to get the last few lines? Why not modify the same command and have both as part of the same command?

So, while I knew quite a few commands in Linux, the only time I started appreciating it is when I saw some of my colleagues using it. My colleagues were masters of the Linux environment! They knew how to intelligently combine these commands to extract value out of them. That's what opened my eyes. The commands were not new to me. But the way my colleagues combined them was intriguing, something I had never thought about.

That is what made me think, there must be some method to this madness. There must be some thought-process behind the design of these commands. It is not random. It's not like someone decided, let's have a command to get the first few lines of a file. I wanted to know what that thought-process was!

So, while I knew quite a few commands in Linux, the only time I started appreciating it is when I saw some of my colleagues using it. My colleagues were masters of the Linux environment! They knew how to intelligently combine these commands to extract value out of them. That's what opened my eyes. The commands were not new to me. But the way my colleagues combined them was intriguing, something I had never thought about.

That is what made me think, there must be some method to this madness. There must be some thought-process behind the design of these commands. It is not random. It's not like someone decided, let's have a command to get the first few lines of a file. I wanted to know what that thought-process was.

That's when I came across this book, The Art of Unix Programming: http://www.catb.org/esr/writings/taoup/html/

This is where Eric Raymond talks about the philosophy of how these commands have been designed.

From the book: "Unix's durability and adaptability have been nothing short of astonishing. Other technologies have come and gone like mayflies. Machines have increased a thousandfold in power, languages have mutated, industry practice has gone through multiple revolutions — and Unix hangs in there, still producing, still paying the bills, and still commanding loyalty from many of the best and brightest software technologists on the planet."

Although, the above paragraph uses the word "Unix", note that this is applicable to Linux as well. Perhaps a better word would be POSIX systems (that includes macOS and Linux).

https://en.wikipedia.org/wiki/POSIX

You will see how these philosophies make a difference in the design of the Operating System and the way you use it.

Here is one of the philosophies, the Rule of Silence. In simple terms, the Rule of Silence says, when there is nothing to say, say nothing.

How is this rule implemented in some commands?

In Linux, here is an actual run of a few commands:

```
john@neo:/tmp$ mkdir foo
john@neo:/tmp$ ls foo
john@neo:/tmp$ rmdir foo
john@neo:/tmp$ 
```

Look at the first command, `mkdir foo`, which is used to created a directory called foo. After we execute this command, Linux silently brought the prompt back; it didn't print anything. It didn't say something like "Directory foo successfully created!" The command `ls` is used to list the contents of the directory. When running this command, Linux didn't tell me, "The directory foo is empty". It rather silently brought us back to the prompt. The fact that the directory is empty is implicit, because if it did have something Linux would have printed it. Even for things like `rmdir` which removes a directory, Linux didn't show any nudges. You asked Linux to do something, it did it, and there was no reason to tell you that it did what you asked it to do! This is the Rule of Silence. Linux is following our commands as if to say, "You know what you are doing, and your wish is my command!"

Why is the Rule of Silence useful?

The very fact that we have rule of silence allows us to combine these commands in interesting ways.

Consider the following sequence of commands:

```
john@neo:/tmp$ mkdir foo
john@neo:/tmp$ touch foo/file1
john@neo:/tmp$ touch foo/file2
john@neo:/tmp$ touch foo/file3
john@neo:/tmp$ ls foo | wc -l
3
john@neo:/tmp$ 
```

We create a directory called foo, then create 3 files in it, file1, file2 and file3. We are now running a command `ls foo | wc -l`. This is a combination of 2 commands - `ls` to list the contents of a directory and `wc` which is used to get character/word/line count (the -l helps us get the line count). The `|` symbol is used to send the output of a command as input to another command. `ls` command prints the names of the 3 files and when we send the output of this command to the `wc -l`, it counts the number of lines in the output of the previous command, which happens to be 3.

Now what if the directory was empty?

```
john@neo:/tmp$ mkdir foo
john@neo:/tmp$ ls foo | wc -l
0
john@neo:/tmp$ 
```

It works equally well! This was possible because of the rule of silence and ls didn't print anything unnecessary.

Now, what happens in case there is an error?

```
john@neo:/tmp$ mkdir foo
john@neo:/tmp$ mkdir foo
mkdir: cannot create directory ‘foo’: File exists
john@neo:/tmp$ ls bar
ls: cannot access 'bar': No such file or directory
john@neo:/tmp$  
```

So, when there is something important to say, you have to say it too and we can trust that the commands will inform us when something goes wrong.

This also uses another philosophy: "Rule of Composition: Design programs to be connected with other programs."

In a world where things get outdated so quickly, if you have followed these rules, there is a possibility that something you developed can survive for a very long time. A very good example of this is the `grep` command.

If you visit the Wikipedia page of the grep command, you will see that it was invented in 1973! Can you imagine that? A technology invented 46 years ago (as of this writing) and is still going strong, and is still not outdated? Almost every Linux system out there and even Mac's ship with a grep command and this is a command we use regularly. What makes this command "stick"? What's the secret of its longevity? This has been explained in the following paragraph from the book:

Doug McIlroy, the inventor of Unix pipes and one of the founders of the Unix tradition, had this to say at the time [McIlroy78]:

(i) Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new features.

(ii) Expect the output of every program to become the input to another, as yet unknown, program. Don't clutter output with extraneous information. Avoid stringently columnar or binary input formats. Don't insist on interactive input.

(iii) Design and build software, even operating systems, to be tried early, ideally within weeks. Don't hesitate to throw away the clumsy parts and rebuild them.

(iv) Use tools in preference to unskilled help to lighten a programming task, even if you have to detour to build the tools and expect to throw some of them out after you've finished using them.

"Do one thing, but do it well" - isn't this what elders advice the juniors in the family? 🤔

The grep command does one thing - it searches for a pattern in the given input (like a file). Because it has done only this one thing, but it has done it well, it has perhaps survived all these years!

You can refer to this Wikipedia page: https://en.wikipedia.org/wiki/Unix_philosophy