"""Write a function that takes a list of strings as input and returns the 
length of the longest common suffix of all the strings. For example, given 
the input ["forest", "best", "crest"], the function should return 3, 
because "est" is the longest common suffix of all the strings."""
import os
def longest_common_suffix(list_of_strings):
	reversed_strings = [' '.join(s.split()[::-1]) for s in list_of_strings]
	print(reversed_strings)
	reversed_lcs = os.path.commonprefix(reversed_strings)
	print(reversed_lcs)
	lcs = ' '.join(reversed_lcs.split()[::-1])
	return lcs

print(longest_common_suffix(["forest", "best", "crest"]))	
