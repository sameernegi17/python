'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.
Input strings will always be well-formed with matching ()s.

•	For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
•	For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
•	For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
•	For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''

def reverseInParentheses(inputString):
    char = list(inputString)
    open_branket = []
    for i,c in enumerate(char):
        if c == '(':
            open_branket.append(i)
        elif c == ')':
            j = open_branket.pop()
            char[j:i] = char[i:j:-1]
    return ''.join(c for c in char if c not in'()')
            


if __name__ == "__main__":
    print(reverseInParentheses("foo(bar)baz"))
