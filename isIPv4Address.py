'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
Given a string, find out if it satisfies the IPv4 address naming rules.
Example
•	For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;
•	For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.
316 is not in range [0, 255].
•	For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.
There is no first number.
'''
def isIPv4Address(inputString):
    char_list= inputString.split('.')
    
    if(len(char_list) !=4):
        return False
    
    for i in char_list:
        if(len(i) > 1 and i[0] == '0'):
            return False
        elif i.isdigit() and 0 <= int(i) <= 255:
            continue
        else:
            return False
        
    return True

if __name__ == "__main__":
    print(isIPv4Address("172.16.254.1"))
    print(isIPv4Address(".16.254.1"))
    print(isIPv4Address("00.16.254.1"))
    print(isIPv4Address("172.16.01.1"))