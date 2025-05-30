Imagine we are trying to add 2 numbers. We can write some code like this:

```python
a = 10
b = 20
c = a + b
```

Let us understand what we are trying to do here line by line:

```python
a = 10
```

We are telling the system to store a value "10" in the RAM (we refer to RAM as memory from now on). Note that the value 10 is stored in its binary form: `1010` in memory. Depending on the programming language, we may also pad this with some bits to convert it into a "byte" like this: `00001010`.

RAM addresses are very long and hard to remember, so we would like to refer to the location where this value is stored with a name, `a` because that's more memorable for us. We refer to such names as "variable names" or simply "variables". We say, `a` is a "variable".

Now how does our system know what this sequence of 0's and 1's means? Is it a number or is it something else? This interpretation is given by what are called "data types". We say that the value that "a" is referring to is of type "number".

So, to summarize, what are we saying in the statement above?

We are saying, "Create a value 10 of type "number" in memory and let "a" be the variable that we use to refer to the location where this number is stored".

Here is another example:

```python
name = "John"
```

What we saying in the statement above?

We are saying, "Create a value "John" of type "string" (simply, a sequence of alphabets or numerical characters) in memory and let "name" be the variable that we use to refer to the location where this string is stored".

Let us now see the next statement:

```python
b = 20
```

The above statement is saying, "Create the value 20 in memory of type number and let "b" be the variable that we use to refer to the location where this number 20 is stored".

The next statement is:

```python
c = a + b
```

We are asking the system to add the 2 numbers `a` and `b` and the result of this should be stored in another location. This location will be referred to using the variable "c". Note that this has a different meaning from mathematical equations. The `=` symbol in most programming languages means "assignment". We are asking the system to assign the value of `a + b` to the location `c`.

In the above statement, `+` is called an operator, and `a` and `b` are its operands. Since `a` and `b` are referring to numbers, the system understands that `+` is supposed to "add" the 2 numbers.

Note the sequence of operations when we say `c = a + b`:

- To begin with `a` and `b` are in the RAM
- The addition operation takes place in the CPU, so for this, the values of `a` and `b` have to be loaded from the CPU to the RAM
- The addition operation then takes place in the CPU and results in the creation of the sum of `a` and `b` in the CPU
- This result is then loaded back into the RAM from the CPU