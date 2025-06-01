def find_duplicates_and_non_duplicates(input_file):
    non_duplicates = []
    duplicates = []
    
    for name in input_file:
        if input_file.count(name) == 1:
            non_duplicates.append(name)
        else:
            if name not in duplicates:
                duplicates.append(name)
    
    print("Non-duplicates:\n")
    
    for name in non_duplicates:
        print(name)
        
    print("\nDuplicates:\n")
    
    for name in duplicates:
        print(name)



input_file = ["Jack", "John", "Jeff",  "Jonah", "Jack", "Jonah"]

find_duplicates_and_non_duplicates(input_file)
