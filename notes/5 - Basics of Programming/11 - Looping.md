Sometimes, we may want to execute a certain set of statements again and again until some condition is true:

```python
1. i = 0
2. while i < 5:
3.   print(i)
4.   i = i + 1
5. print('Done!')
```

The statement in line 2 is the beginning of a loop. A loop is a way we are telling the system to do something repeatedly. What do we want the system to repeat? Answer: The next 2 lines (3 and 4).

How does the system know what to repeat?

Note the indentation of line 3 and 4. Note also that the indentation for line 3 and 4 is exactly the same (2 spaces each).

Till when should we run these statements repeatedly?

Answer: Loops have a condition that tells the system until when it is supposed to repeat the statements. In our current example, the condition is `i < 5`. We run the statements in the loop (line 3 and 4) until the condition `i < 5` mentioned in line 2 no longer holds true.

Let us now understand this step by step:

- We create a value 0 and assign it to a variable `i`
- We now encounter the `while` loop, which tells the system that we want lines 3 and 4 to run repeatedly until the condition `i < 5` is no longer true. The system now checks the condition. Is the value of i less than 5? If so, run the statements in the loop, if not go to the next statement after the loop (line 5).
- Since the current value of i is 0 and 0 is less than 5, the system starts running the statements in the loop starting from line 3.
- Line 3 asks the system to print the current value of i to the console. So we will see the value 0 appear on the screen.
- We then move to the next statement - which increments the value of i by 1. The value of i now becomes 1.
- Remember that we are "inside" a loop and our work is not done, so we now have to "jump back" to line 2. The system now checks the condition again. Is the value of i less than 5? The current value of i is 1, which is still less than 5. So the statements in the loop run again. The current value of i, 1, is printed to the console. The value of i is incremented by 1 and i becomes 2.
- The process repeats and we see the values 2, 3 and 4 getting printed to the console.
- At this point the value of i becomes 5. Is the current value of i less than 5? Note that 5 is not less than 5. So the condition check fails. So the loop stops and the next statement after the loop (line 5) runs.
- We now see the system printing "Done!" in the console.