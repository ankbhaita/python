"""Write a function that takes a list of integers as input 
and returns the longest increasing subsequence of the list. 
For example, given the input [3, 1, 4, 2, 5, 3], 
the function should return [1, 2, 3, 5]."""
st = []
def find_lon_subsquence(inp, out) :
    if len(inp)== 0 :
        if len(out) != 0 :
            st.append(out)
        return
 
    find_lon_subsquence(inp[1:], out[:])
 
    if len(out)== 0:
        find_lon_subsquence(inp[1:], inp[:1])
    elif inp[0] > out[-1] :
        out.append(inp[0])
        find_lon_subsquence(inp[1:], out[:])
 
find_lon_subsquence([3, 1, 4, 2, 5, 3], [])
longest_sub=sorted(st, key = len)
for i in reversed(range(len(longest_sub)-1)):
    if len(longest_sub[len(longest_sub)-1])!=len(longest_sub[i]):
        break
    print(longest_sub[i])
    

