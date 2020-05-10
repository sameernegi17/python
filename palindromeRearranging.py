'''
Given a string, find out if its characters can be rearranged to form a palindrome.
Example
For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.
We can rearrange "aabb" to make "abba", which is a palindrome.
'''
def palindromeRearranging(inputString):
    dict_char = {}
    
    for i in inputString:
        if i in dict_char:
            dict_char[i] = dict_char[i] + 1
        else:
            dict_char[i] = 1
            
    count = 0
    for value in dict_char.values():
        if(value % 2 != 0):
            count = count + 1
            
    if (count > 1):
        return False
    else:
        return True



if __name__ == "__main__":
    print(palindromeRearranging("aabb"))
    print(palindromeRearranging("aabbc"))
    print(palindromeRearranging("aabbcd"))