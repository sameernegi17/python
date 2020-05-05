if __name__ == "__main__":

  option = int(input("Enter the Option 1 . perimeter 2 . Area "))
  side = int(input("Enter the side"))
  if(option == 1 and side > 2):
      print(side * side)
  elif(option == 2 or side > 2):
      print(4 * side)
  else:
      print("That you have entered the wrong option")
      
