
def sum_list(number):
    n = 0
    sum_number = 0
    while(n < len(number)):
        sum_number += int(number[n])
        n = n + 1
    return sum_number

def isLucky(num):
    number = list(str(num))
    center = len(number) // 2
    result1 = sum_list(number[0:center])
    result2 = sum_list(number[center:])
    if(result1 == result2):
        return True
    else:
        return False


if __name__ == "__main__":
    print(isLucky(1230))