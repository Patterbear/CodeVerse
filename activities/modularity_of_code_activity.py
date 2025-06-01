def fibonacci(n):
    count = 0
    a = 0
    b = 1
    
    while count < n:
        print(a)
        
        temp = a
        a = b
        b = temp + b
        
        count += 1

fibonacci(5)
