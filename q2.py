class Stringsorter: 
        def selection_self(self,string_list):
         n=len(string_list)
         for i in range(n):
             minindex=i
             for j in range(i+1,n):
                 if string_list[j]<string_list[minindex]:
                     minindex=j
             string_list[i],string_list[minindex]=string_list[minindex],string_list[i]
         return string_list
my_words=["zebra","apple","banana"]
sorter_objects=Stringsorter()
sorted_words=sorter_objects.selection_self(my_words)
print(sorted_words)

           
                     

                     
   
