#import random module with 'r' as its alias
import random as r

print("WELCOME!!")

#Giving the information to user
print("Enter 1 for choosing Rock \n Enter 2 for choosing Paper \n Enter 3 for choosing Scissors\n")

while True:
    #take the input from user
    user_ch=int(input("Enter your choice"))
    #initializing the value of user_ch variable
    if(user_ch==1):
        print("You have chose Rock!\n") #priting the user choice accordingly elif(user_ch==2):
        print("You have chose Paper!\n")
    else:
        print("You have chose Scissors!\n")
        print("Now it's turn for computer's Choice\n")

 #initializing the value of cp_ch variable
 #computer will randomly choose any number among 1,2,3
    cp_ch=r.randint(1,3) #Using randint method of random module
    if(cp_ch==1):
        print("Computer's choice: Rock!\n") #printing the random computer'schoice
    elif(cp_ch==2):
        print("Computer's choice: Paper!\n")
    else:
        print("Computer's choice: Scissors!\n")
 #Conditions to win
    print("Now it's Time to Play")

    if((user_ch==1 and cp_ch==2) or (user_ch==1 and cp_ch==3) or(user_ch==3 and cp_ch==2)):
        print("User wins!!")
    elif((user_ch==2 and cp_ch==1) or (user_ch==2 and cp_ch==3)or
        (user_ch==3 and cp_ch==1)):
            print("Computer wins!!")
    #checking for draw
    elif(user_ch==cp_ch):
        print("It's a tie!")
 #asking user to play more
    print("Do you want to play again(Y/N)?")
    a=input()
 #if input is N then the condition will be true and loop continues
    if(a=='N'):
        break
    print("Thanks for playing!")