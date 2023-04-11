"""Write a function that takes a list of integers as input and returns the 
maximum sum of any contiguous subarray of the input list. For example, 
given the input [-2, 1, -3, 4, -1, 2, 1, -5, 4], the function should 
return 6, because the maximum sum is achieved by the subarray [4, -1, 2, 1].
Note that the subarray must be contiguous (i.e., all the elements are 
adjacent in the original list)."""

def sum_con_subarray(arr_list):
	lists = [[]]
	sum_num=0
	index_num=0
	for i in range(len(arr_list) + 1):
		for j in range(i):
			lists.append(arr_list[j: i])
	for i in range(len(lists)):
		if sum_num<=sum(lists[i]):
			sum_num=sum(lists[i])
			index_num=i

	return lists[index_num]		
		
	
    
        
            
     
    
print(sum_con_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))    
