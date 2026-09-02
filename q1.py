n=int(input("Enter a number"))
string_list=[]
for i in range(n):
                  user=input(f"Enter string {i+1}: ")
                  string_list.append(user)
counts={}
for word in string_list:
        for char in word:
                if char.isalpha():
                    lower_char=char.lower()
                    if lower_char in counts:
                      counts[lower_char]+=1
                    else:  
                      counts[lower_char]=1
print(counts)