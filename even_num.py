"""Write a function that takes a list of integers as input and returns a new list containing only the even numbers from the original list."""
def even_num(int__list):
	b=[x for x in int__list if x%2==0]
	return b

print(even_num([2,4,5,9,8,3,12,20]))	
	
