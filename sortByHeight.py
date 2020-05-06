'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!
Example
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''

def sortByHeight(a):
    numer_list = [x for x in a if x != -1]
    numer_list.sort()
    
    result = []
    k = 0
    for element in a: #[-1, 150, 190, 170, -1, -1, 160, 180]
        if element == -1:
            result.append(-1)
        else:
            result.append(numer_list[k])
            k = k + 1
    return result


if __name__ == "__main__":
    height = [-1, 150, 190, 170, -1, -1, 160, 180]
    print(sortByHeight(height))