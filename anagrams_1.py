"""How would you write a Python function that takes a list of words as input and returns a list of lists, where each sublist contains all the anagrams of a particular word in the input list?
input: ['souep', 'eat', 'node', 'ate', 'done', 'tea']
output: [["souep"],["eat", "ate", "tea"],["node", "done"]]"""

def list_anagram(input_list):
	dic={}
	for i in input_list:
		w="".join(sorted(i))
		if w in dic:
			dic[w].append(i)
		else:
			dic[w]=[i]
	print(list(dic.values()))
	
list_anagram(['souep', 'eat', 'node', 'ate', 'done', 'tea'])			
			

