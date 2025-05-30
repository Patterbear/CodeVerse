# Introduction

Time complexity is basically a way of measuring how much time it takes to perform some operation.

Consider an array of numbers. Let's say we are trying to find the number at a specific position. How long does it take to get this item?

The time taken is constant in an array because you can jump to any location in an array in a constant amount of time. The reason is, an array uses pointer arithmetic to locate an item. So, the time complexity of this algorithm is constant or O(1).

Now, let's say you are trying to add numbers in an array. You will need to look at it one item at a time. How long does it take for you to add the numbers? The time it takes is directly proportional to the number of items in the array, right? Such an algorithm is said to have a time complexity of 0(n) or linear time complexity. As the number of items increases, the time taken also increases proportionally.

You then have algorithms where the time taken is n^2 or quadratic. For eg, if you have to compare every number in an array with every other number, such an algorithm is said to have n^2 complexity.

# Time complexities of various collections

Once you understand implementations of various algorithms, you will see that the time complexity of looking up an item at a specific position in a list is constant if the list is implemented using an array. Similarly, the time complexity of looking up a key in a map to get its value takes constant time if the map is implemented using a hashtable.