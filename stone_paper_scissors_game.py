a = "stone"
b = "paper"
c = "scissors"


# lets take users input
user_01 = input("enter your choise: ")
user_02 = input("enter your choise: ")

# now make the logic for game
if (user_01 == user_02):
    print("tie")

elif ( (user_01 == a and user_02 == c) or (user_01 == b and user_02 == a ) or (user_01 == c and user_02 == b) ):
    print("user_01 wins")

elif ( (user_01 == a and user_02 == b) or (user_01 == b and user_02 == c) or (user_01 == c and user_02 == a)):
    print("user_02 wins")

else:
    print("error!!\ninvaid input")