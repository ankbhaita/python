"""Write a function that takes a list of strings as input and returns 
a new list containing only the strings that have at least one uppercase 
character."""

def str_uppercase(str__list):
	u_s=[]
	
	for x in range(len(str__list)):
		b_s=False
		for i in str__list[x]:
			if i.isupper():
				print(i)
				b_s=True
				break
		if b_s:
			u_s.append(str__list[x])
			
	return u_s
print(str_uppercase(['Ankita','ram','Shyam','Ariya','Mohan']))	
