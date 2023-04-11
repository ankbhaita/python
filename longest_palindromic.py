"""Write a function that takes a string as input and returns the 
longest palindromic substring of the string. For example, given the 
input "babad", the function should return "bab" or "aba"."""           	
def longest_palindromic(arr_list):
    lists = [[]]
    pele_list=[]
    for i in range(len(arr_list) + 1):
        for j in range(i):
            lists.append(arr_list[j: i])

    for j in range(1,len(lists)):
        revstr=""
        string=lists[j]
        for i in string:
            revstr=i+revstr
        if string==revstr:
            pele_list.append(string)
   
    list_sub_peli_sort=sorted(pele_list, key=len)

    max_len_pali_list=[]
    max_len_pali=len(list_sub_peli_sort[len(list_sub_peli_sort)-1])
    for i in reversed(list_sub_peli_sort):
        
        if len(i)==max_len_pali:
            max_len_pali_list.append(i)
        else:
            break

    print(max_len_pali_list)              

longest_palindromic('babad')        
            

