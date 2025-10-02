# # 1 for snake
# # -1 for water 
# # 0 for gun


# computer=-1
# youstr=input("enter your choice:")
# youDict={
#     "s":1,
#     "w":-1,
#     "g":0
# }
# you=youDict[youstr]

# if(computer==-1 and you==1):
#     print("you win")

# elif(computer==-1 and you==0):
#     print("you loose")

# elif(computer==1 and you==0):
#     print("you win")

# elif(computer==1 and you==-1):
#     print("you loose")

# elif(computer==0 and you==1):
#     print("you loose")

# elif(computer==0 and you==-1):
#     print("you win")

# else:
#     print("Something went wrong");


import random

# 1 for Snake, -1 for Water, 0 for Gun
choices = {1: "Snake", -1: "Water", 0: "Gun"}

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
you = youDict.get(youstr, None)

if you is None:
    print("Invalid input!")
else:
    print(f"Computer chose: {choices[computer]}")
    print(f"You chose: {choices[you]}")

    if computer == you:
        print("It's a Tie!")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You Win!")
    else:
        print("You Lose!")



