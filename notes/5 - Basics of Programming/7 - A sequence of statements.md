Here is a way to tell the system to add 2 numbers, `a` and `b` and then print their result to the screen:

```python
a = 10
b = 20
c = a + b
print(c)
```

A program written in a programming language contains a sequence of statements like above.

Do the order of the statements matter?

Yes! In most languages, the statements get executed from top to bottom.

Let us take up some examples to understand this.

```python
a = 10
b = 20
a = a + b
b = a + b
```

After this sequence of statements are executed, what is the value of `a` and `b`?

Let us understand it step by step:

- We first create a value 10 and call it `a`
- We then create the value 20 and call it `b`
- We then add the value of `a` and `b` and store it in the location `a` - so `a` gets the value 30.
- We then add the current value of `a` and `b` and store it in the location `b` - so `b` gets the value 50.

So the final value of `a` is 30 and the final value of `b` is 50.

Now what if we wrote the statements in this order:

```python
a = 10
b = 20
b = a + b
a = a + b
```

What is the value of `a` and `b` after these statements are executed?

Let us understand it step by step:

- We first create a value 10 and call it `a`
- We then create the value 20 and call it `b`
- We then add the value of `a` and `b` and store it in the location `b` - so `b` gets the value 30.
- We then add the current value of `a` and `b` and store it in the location `a` - so `a` gets the value 40.

So the final value of `a` is 40 and the final value of `b` is 30.

Clearly, the order of statements matter.

A program is made up of a sequence of statements. As the statements execute, they make changes to some locations. The changes made by a certain statement affects the next statement.