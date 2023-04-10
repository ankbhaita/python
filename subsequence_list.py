"""Write a function that takes a list of integers as input and returns 
the longest increasing subsequence of the list. For example,
 given the input [3, 1, 4, 2, 5, 3], the function should return [1, 2, 3, 5].
 """
"""Write a function that takes a list of integers as input and returns 
a new list containing all the unique triplets that sum to zero. 
For example, given the input [-1, 0, 1, 2, -1, -4], the function should 
return [[-1, 0, 1], [-1, -1, 2]]."""

 def Zero_Triplets(num_list):
    triplet_list = []
    n=len(num_list)
    for i in range(0, n-2):
 
        for j in range(i+1, n-1):
 
            for k in range(j+1, n):
 
                if (num_list[i] + num_list[j] + num_list[k] == 0):
                	triplet_list.append([num_list[i],num_list[j],num_list[k]])

     print(triplet_list) 
 
 Zero_Triplets([-1, 0, 1, 2, -1, -4])              	
                    
