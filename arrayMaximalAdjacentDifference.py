'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
'''

def arrayMaximalAdjacentDifference(inputArray):
    abs_difference = 0
    for i in range(1,len(inputArray)):
        difference = abs(inputArray[i-1] - inputArray[i])
        if(difference > abs_difference):
            abs_difference = difference
    
    return abs_difference

if __name__ == "__main__":
    print(arrayMaximalAdjacentDifference([2, 4, 1, 0]))


