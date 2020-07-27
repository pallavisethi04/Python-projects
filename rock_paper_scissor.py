import random as rd

options = ["rock", "paper", "scissor"]

choice= input("Make you selection:")
choice= str(choice)
choice= choice.lower()
print("Your choice:", choice)
Computer= str(rd.choice(options))
Computer= Computer.lower()
print("Computer Choice:",Computer)
if choice in options:
    if choice == Computer:
        print("Its a tie")
    if choice== "rock":
        if Computer== "paper":
           print("You Win1")
        elif Computer== "scissor":
           print("You Loose1")
    if choice== "paper":   
        if Computer== "rock":
            print("You Win2")
        elif Computer== "scissor":
            print("You Loose2")
    if choice== "scissor":
        if Computer== "paper":
            print("You Loose3")
        elif Computer== "rock":
            print("You Win3")
else:
    print("Invalid selection, Try again!!")

		


    
    
