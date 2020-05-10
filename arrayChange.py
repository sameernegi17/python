'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
Example
For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
'''
def arrayChange(a):
    sum = 0
    q = a[0]
    for i in a[1:]:
        if(i <= q): #[1,1,1] [1,2,3]
            sum += q - i + 1  # q = 1 i =1 2) q = 2 i =1
            q = q + 1
        else:
            q = i
            
    return sum


if __name__ == "__main__":
    print(arrayChange([1,1,1]))
    print(arrayChange([-1000,0, -2 , 1 ,3]))# -1000 ,0,1,2,3