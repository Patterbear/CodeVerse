Sometimes, we may want to skip a few statements based on a condition:

```python
1. i = 10
2. if i < 5:
3.   print('i is less than 5')
4. print('Done!')
```

The statement in line 2 is what we refer to as a conditional. A conditional is a way of telling the system to check something and only execute some statements if the condition holds true.

What is the condition we want the system to check?

Answer: 'if i < 5' means "Is the value of i less than 5".

What do we want the system to do if the condition is true (i.e. if the value of i is less than 5)?

Answer: We want it to execute the next statement - "print('i is less than 5')".

How does the system know which statement(s) to run if the condition is true?

Note, how in line 3, we have moved the code slightly to the right. We call this as "indentation" in a language. Doesn't this give us an impression of a hierarchy? It looks like this line is "inside" the previous line. We say the statement - `print('i is less than 5')` is inside the `if` condition.

Indentation is the empty space to the left of the code. We can say that line 3 has an indent of 2 spaces. Indentation can be done using either tabs or spaces.

Let us now summarize the above code step by step:

- Line 1: We create a value 10 and assign it to a variable `i`
- Line 2: We encounter the `if` condition, which tells the system to check if the condition `i < 5` is true. If so, we want it to execute statement in Line 3, if not, skip Line 3 and jump to Line 4. The system now checks the condition. Is the value of i less than 5? Since this is false, Line 3 is skipped.
- We move to the next statement on Line 4 and the system prints "Done!" in the console.

Here is another example:

```python
1. i = 0
2. if i < 5:
3.   print('i is less than 5')
4. print('Done!')
```

Let us understand this step by step:

- Line 1: We create a value 10 and assign it to a variable `i`
- Line 2: We now encounter the `if` condition, which tells the system to check if the condition `i < 5` is true. If so, we want it to execute statement in Line 3, if not, skip Line 3 and jump to Line 4. The system now checks the condition: "Is the value of i less than 5?" Since this is true, we execute Line 3 next.
- Line 3 asks the system to print the statement "i is less than 5" to the console.
- We move to the next statement on Line 4 and the system prints "Done!" in the console.

Here are some more examples of condition checks:

- `if i != 10` - In a lot of languages `!=` is read (and means) "not equal to". So we are saying "if the current value of i is not equal to 10 then run the indented statements".
- `if a % 2 == 0` - In a lot of languages `%` stands for the modulus operator. This condition says "when you divide `a` by `2` if the remainder is `0`, then run the indented statements". In other words, "if `a` is an even number run the indented statements".
- `if a % 2 != 0` - This is a way of saying, "if `a` is an odd number, run the indented statements".

What if we want the system to do one thing if a condition is true and a different thing if the condition is false. Programming languages have something called an if-else condition for this.

Here is an example:

```python
1. i = 5
2. if i <= 5:
3.   print('i is less than or equal to 5')
4. else:
5.   print('i is greater than 5')
6. print('Done!')
```

Here is another example of if/else:

```python
1. i = 25
2. if i <= 5:
3.   print('i is less than or equal to 5')
4. else:
5.   print('i is greater than 5')
6. print('Done!')
```