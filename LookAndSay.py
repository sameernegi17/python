

def countNext(char):

    output = ""
    char += "$"
    count = 1
    curr_char = char[0]
    for idx in range(1,len(char)-1):
        if curr_char != char[idx]:
            output += str(count) + curr_char
            count = 1
            curr_char = char[idx]
        else:
            count +=1

    output += str(count) + curr_char
    return output


def lookAndSay(N):

    if N == 1:
        return '1'

    N-=1

    a = "1"
    while N > 0:
        a = countNext(a)
        N -= 1

    return a


print(lookAndSay(6))
