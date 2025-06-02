There are so many commands in Linux that we will need instant access to documentation and some help on using the commands. Here are some things to remember about getting help in a Linux environment.

Let's say I want to know more about the command `ls`, what does this command do, how do I use it, what switches I can use with this command etc.

To get help, you can access the manual (or the man page) of this command.

You can get the manual of `ls` by typing:

```bash
man ls
```

Since the manual is very large, the output opens in a pager. Otherwise, the entire contents would scroll so quickly that you wouldn't be able to read it unless you have some superpowers.

The pager environment shows you a screen-full of content at a time and you can then page through the contents, hence the name. The preferred way to scroll through the content is using some keyboard shortcuts (eg: j to move one line down, k to move a line up) and these are all similar in various environments including a popular editor in Linux called the `vi` editor.

You can use the keyboard's down and up arrow keys to move up and down through the content too. In a GUI which has a mouse, you can scroll using the mouse as well. So you may wonder why these strange keys? The reason is, these environments are designed such that you can minimize the mouse usage and also, to not have to move your hands away from the regular position of your hands over the keyboard. Now, this is true, for people who know touch typing.

💡 If you are serious about improving your productivity with programming skills and plan to use a keyboard to write code, it is perhaps a good idea to learn touch typing! (I believe that we will be using a keyboard to write code at least into the foreseeable future unless Alexa/Siri get really intelligent and can do that for us).

### A bit about Keyboards, QWERTY, Typewriters and Touch Typing

Most keyboards we use today are called QWERTY keyboards. The name QWERTY comes from the order of the first six keys on the top left letter row of the keyboard.

Computers came later, keyboards came first (actually I am talking about typewriters 😊). A typewriter does not have a cursor, so there are no arrow keys or special characters. So, the characters found in a typewriter are found in the same position in a modern day computer keyboard too while all other characters have had to take up the remaining places around these keys. In fact, early computers like the https://en.wikipedia.org/wiki/ADM-3A did not have arrow keys.

💡 According to Wikipedia, the weird arrangement of the keys in a QWERTY keyboard could be to reduce the likelihood of internal clashing of typebars by placing commonly used combinations of letters farther from each other inside the machine - although we are unsure if this is a true story. However, one thing I can tell you is that, we have learned to type at a really rapid pace on these keyboards despite the weird arrangement of characters! Hats off to humans who can get used to anything!

The initial position of your hands in a QWERTY keyboard is such that the little finger of your left hand is positioned on the character `A`, the ring finger on `S`, the middle finger on `D` and the forefinger on `F`. Similarly, the little finger of the right hand is positioned over the character `;`, the ring finger on `L`, the middle finger on `K` and the forefinger on `J`. So when you type these characters you are supposed to be using these fingers. The `G` is typed with the left forefinger itself, and the `H` is typed with the right forefinger.

![[QWERTY-home-keys-position.svg.png]]

Now, if you observe carefully, the characters `F` and `J` have a small bump in the keyboard. The reason these bumps exist is so that you can position all your fingers and know that you have aligned it right by feeling these bumps with your forefinger. Once aligned, you can then start typing without having to look at the keyboard.

Now observe the initial position of the fingers of your right hand. They are over the characters, J, K, L and ; and even H is very accessible in this position.

For a touch typist, moving the hands to the arrow keys and back is a waste of time and can hamper productivity. So imagine I open the man page of a command and then I have to scroll through the content. It is easier for me to scroll the content using the keys `j`/`k` than to have to move my right hand to the arrow keys and back. Switching between keyboard and mouse also takes time.

The `vi` shortcuts and the shortcuts used in these pagers are derived from this fact.

Here are the keyboard shortcuts that you can use in the pager:

- `j` to scroll one line down
- `k` to scroll one line up
- `Shift+G` to go to the end
- `g` to go to the top
- `/` to begin your search
- Type the characters that you want to search after `/`. Eg: `/directory↲`
- Use `n` to search the next occurrence
- `Shift+N` to search previous occurrence
- `q` to quit

All these keyboard shortcuts should become second nature to you and that is when you will start feeling the Linux environment very differently.

💡 Did you know that these same keyboard shortcuts (like `j`/`k` and `/` to search) can also be used in Gmail/Twitter/GitHub etc?

### Using --help

Another way to get help is by using the switch `--help`.

Here are some examples:

- `ls --help`
- `ps --help`
- `bash --help`
- `vim --help`

This is useful for a quick reference to the switches and to know the arguments that you can pass to a command and the output you can expect.

Unlike the output of `man`, the output of `--help` scrolls even if it is long. The keyboard shortcut to scroll up/down the terminal output is `Shift+PgUp` and `Shift+PgDown`. But we have seen that the pager output can be more user friendly to scroll because I can scroll a line at a time, a page at a time, I can easily move to the beginning, end, I can search etc.

So what we can do is to pass the output of the command to a pager like `less`.

```
ls --help | less
```

You will now see that this behaves similar to the man output. You can use the same keyboard shortcuts as in the man output.