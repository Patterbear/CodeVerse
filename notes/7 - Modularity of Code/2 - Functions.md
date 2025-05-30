# Functions

One thing you can do is to divide the entire program into functions (or methods or sub-routines or procedures). Every function has a clear purpose.

In your high-school, you must have learnt about functions in mathematics. A function is something that takes some input and provides some output, so there is some correspondence between the input and the output.

Functions in Programming Languages are similar. They take inputs and they provide outputs.

A function is sort of like a contract - imagine the function speaking to you - "If you give me this input, I will give you this output. If you give me a number, I will give you its square-root. If you give me the name of a person, I will tell you if he works in this company or not".

So what are the things we need when creating a function:

- We need a name for the function
- We need to have clearly defined inputs
- We need to have clearly defined outputs
- We finally need to have a definition - which is how the function already works

Here is an example of a function:

```
function square(x):
    return x * x
```

Name of the function is square It takes x as input and x should be a number It returns the square of x as output and that is a number too

You can then "call" the function as follows:

```
square(4)
square(10)
```

etc

Can I "call" a function within another function? Yes you can

Can I call the same function from within the function? Yes you can and they are called recursive functions

# More

- [http://en.wikipedia.org/wiki/Procedural_programming](http://en.wikipedia.org/wiki/Procedural_programming)