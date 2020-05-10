'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.
Example
•	For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.
The arrays are equal, no need to swap any elements.
•	For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.
We can obtain b from a by swapping 2 and 1 in b.
•	For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.
Any swap of any two elements either in a or in b won't make a and b equal
'''
def areSimilar(a, b):
    if a == b:
        return True
    
    i = 0
    while(i < len(a)):
        if(a[i] == b[i]):   # [1,2,3] [2,1,3] => [1,2] [2,1]
            a.pop(i)
            b.pop(i)
        else:
            i = i + 1
    
    if len(a) != 2:
        return False
    
    b.reverse()
    
    if a == b:
        return True
    else:
        return False
            
            
if __name__ == "__main__":
    a = [1,2,3,4]
    b = [2,1,4,3]
    print(areSimilar(a,b))