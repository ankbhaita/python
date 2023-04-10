"""How would you write a Python function that takes a list of filenames as input and returns a sorted list of filenames, where each filename is sorted by its extension (i.e., the characters that come after the last period character)?
input: ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
output:['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']"""
from operator import itemgetter
def ext_sort(a):
	file_name=[]
	n_s=[]
	sorted_list=[]
	for i in a:
		n_s=i.split('.')
		file_name.append(n_s)
	b=sorted(file_name,key=itemgetter(1))
	for i in b:
		c=".".join(i)
		sorted_list.append(c)
	print(sorted_list)

ext_sort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

