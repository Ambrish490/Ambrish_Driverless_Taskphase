def open_hashing():
    hash_table = [[] for _ in range(10)]
    
    n = int(input("How many numbers do you want to insert? "))
    
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        index = num % 10
        hash_table[index].append(num)
        
    print("\n--- Final Hash Table ---")
    for i in range(10):
        print(f"Sublist {i}: {hash_table[i]}")


open_hashing()