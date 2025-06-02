The BASH shell comes with several keyboard shortcuts so it's worth your time to learn and master them.

Here are some tips for you:

- Use of arrow keys to find a command that you have entered earlier

Suppose you typed a command and made a mistake. Let's say, you were supposed to type `ls --help`, but you type `ls -help`. Never type the whole command again! Remember that the entire history is available with up and down arrow keys. Just press the up arrow key and you will be able to retrieve the command that you just typed.

- The cursor does not need to be in the end of the line to enter and execute the command

I have noticed that a lot of beginners believe that it is required to position the cursor at the end of the command before you press Enter and execute it. This is not required. The cursor can be anywhere when you enter.

- Use of Ctrl+Left-Arrow or Ctrl+Right-Arrow to move a word at a time

Suppose you have typed a command or retrieved a command from history. Just before you press Enter, you realized that there is a typo in the command and now you need to move your cursor back to the place where the typo exists. You don't need to move your cursor using only left and right arrow keys. You can use Ctrl+Left-Arrow or Ctrl+Right-Arrow to move a word at a time. You can also use Alt+Left-Arrow or Alt+b to move left a word at a time and Alt+Right-arrow or Alt+f to move right a word at a time. You can move to the beginning using Home and to the end using End keys.

- Copy/Paste in the terminal

Did you know that there are ways to cut/copy/paste text in the terminal?

Let's say you made a mistake in a command:

```
touch foo
```

Now you actually meant to type, `touch bar`.

To remove foo and replace with bar, here is what you can do. Press Ctrl+w to remove the word behind the cursor. You can then type `bar`.

Here is an example of cut and paste.

Let's say you typed:

```
foo touch
```

and you meant to type `touch foo`. Press Ctrl-w to cut the word touch. Then position the cursor at the starting of the command (i.e. under f). Now press Ctrl+y.

You can remove all the characters to the right of the cursor using Ctrl+k and all characters to the left using Ctrl+u. Anything removed by Ctrl+k or Ctrl+u is available for paste with Ctrl+y.

You can also use Alt+d to remove the word from cursor to the right.

- Reverse search through history

This one tip can be so useful that you will thank me in future for it!

It's the keyboard shortcut Ctrl+r to reverse search through the BASH history.

Let's say I had run the command `ls --help` sometime back. It may not be the immediate previous command but I know I typed it recently. When I know this, even if it's not the exact same command, I never type the command again.

Press Ctrl+r. Then start typing some characters that you know are present in the command. Eg: Ctrl+r followed by `--help`. As you type, BASH searches through your history and shows you the commands that match the characters that you typed with the most recent command showing up first. If you are able to retrieve the exact same command as what you want to enter now, you can press Enter and it will execute the command. If not, you are always free to modify the command using all the shortcuts that I explained above and then press Enter.

- The `history` command gives you the complete history of all commands that you typed

You can pipe the output of `history` command to `grep` and find only specific commands. Eg:

```
history | grep ls
```

or you can even page through:

```
history | less
```

- Copy/Paste with mouse in a GUI
    
- To copy some text in a GUI, you just have to select it (don't need to press anything like Ctrl+C to copy)! You can also select a word with a double click and a paragraph with a triple click.
    
- The paste depends on the type of touchpad you have.
    
    - If you have a touchpad with 2 physical keys, then you can middle click by pressing both the keys.
    - If you don't have 2 physical keys, you may have to tap 3 fingers together. (This may not be enabled by default in Linux.)
    - If you have an external mouse, you can press the scroll wheel in the mouse.
    - If none of these work, you can try pressing Shift+Insert after you have selected and that should paste too!

In summary, you select to copy and you middle-click to paste.

If none of these works, there is yet another way to copy/paste. You can select the text and press Ctrl+Shift+C to copy and Ctrl+Shift+V to paste. Note that it is not Ctrl+C because this has a different meaning in the terminal (used to send a SIGINT signal to a process which can kill the running process).