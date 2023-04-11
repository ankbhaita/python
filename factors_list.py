"""Write a function that takes a list of integers as input and returns
 a new list containing the same integers, sorted in decreasing order 
 of the number of factors they have. For example, given the 
 input [4, 6, 7, 12, 15], the function should return [15, 12, 6, 4, 7], 
 because 15 has the most factors (4), followed by 12 and 6 (3 factors each),
  then 4 (2 factors), and finally 7 (2 factors)."""

def  factors_list(num_list):
	factor_list=[]
	for i in num_list:
		fac_num=2
		for j in range(2,int((i/2)+1)):
			if i%j==0:
				fac_num+=1
		factor_list.append((i,fac_num))
	sort_factor_list=sorted(factor_list, key=lambda x:x[1],reverse=True)
	factor_list=[x[0] for x in sort_factor_list]
	return factor_list			
								

		
print(factors_list([4, 6, 7, 12, 15]))
		


