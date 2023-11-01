myList = []
while True:
    user_input = input("Enter a number or 'Q' to quit: ")
    if user_input == 'Q':
        break   
    try:
        number = int(user_input) 
        myList.append(number)  
    except ValueError:
        print("Invalid input. Please enter a number or 'Q'.")

print("Number of things in myList:", len(myList))
