class Stringsorter: 
    def selection_self(self, string_list):
        n = len(string_list)
        for i in range(n):
            minindex = i
            for j in range(i+1, n):
                if string_list[j] < string_list[minindex]:
                    minindex = j
            string_list[i], string_list[minindex] = string_list[minindex], string_list[i]
        return string_list

class StringSearcher:
    def binary_search(self, string_list, target_string):
        low = 0
        high = len(string_list) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if string_list[mid] == target_string:
                return mid
            elif string_list[mid] < target_string:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1






n = int(input("Enter a number: "))
my_list = []
for i in range(n):
    user = input(f"Enter string {i+1}: ")
    my_list.append(user)

# 2. Sort it using the Q2 function
sorter_object = Stringsorter()
sorted_list = sorter_object.selection_self(my_list)
print(f"\nSorted list: {sorted_list}")

# 3. Input a string, search for it (Q3 logic)
searcher_object = StringSearcher()
target = input("Enter the string to search for: ")
result_index = searcher_object.binary_search(sorted_list, target)

if result_index != -1:
    print(f"\nSuccess! '{target}' was found at index {result_index}.")
else:
    print(f"\n'{target}' was not found in the list.")