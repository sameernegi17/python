if __name__ == "__main__":
    lst = [1,2,3]
    print(lst[1])
    print(lst[0:2])
    print(lst[::-1])
    print(lst.index(2))
    print(lst.insert(1,10))
    print(lst)
    lst.sort()
    print(lst)
    lst[0] = 12
    print(lst)
    
    tple = (1,2,3)
    print(tple[1])
    print(tple[0:2])
    print(tple[::-1])
    print(tple.index(2))

    
    st = {1,2,3,4,5,4,3,2,1}
    print(st)
    
    # To remove duplicate Elements from the list
    lst = [1,2,3,2,3,4,1]
    st = set(lst)
    lst = list(st)
    print(lst)
    
    
    dit = { 1 : "Abhishek" , 2 : "Sameer", 3 : "yatender"}
    print(dit)
    dit[4] = "Aditya"
    dit[3] = "ishita"
    
    print(dit)
    for i in dit.keys():
        print(i)
        
    for i in dit.values():
        print(i)