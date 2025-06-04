for i in range(1, 100):
    output = ""

    if i % 3 == 0:
        output += "Fast"
    
    if i % 7 == 0:
        output+= "Car"
    
    if output == "":
        output = str(i)

    print(output)