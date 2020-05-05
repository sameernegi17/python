if __name__ == "__main__":
    while(True):
        option = int(input("Enter your option 1. Area 2. Perimeter 3. Print name 4. exit "))
        if ( option < 4):
            if(option == 0):
                print("Wrong option. Please choose the right one")
            else:
                side = int(input("Enter the side"))
                if(option == 1):
                    print("Area of the Square" + str(side * side))
                elif(option == 2):
                    print("Perimeter of the Square" + str(4 * side))
                else:
                    print("My name is Sameer")
                    
        else:
            break
            