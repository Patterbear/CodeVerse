Sometimes we may want to write conditions inside another condition:

```python
1. i = 5
2. if i <= 5:
3.   if i == 5:
4.     print('i is equal to 5')
5.   else:
6.     print('i is less than 5')
7. else:
8.   print('i is greater than 5')
9. print('Done!')
```