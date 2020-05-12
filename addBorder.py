def addBorder(picture):
    result = []
    asterick = '*' * (len(picture[0]) + 2)
    result.append(asterick)
    for i in picture:
        result.append('*' + i + '*')
    
    result.append(asterick)
    return result


if __name__ == "__main__":
    print(addBorder(['abc','def']))