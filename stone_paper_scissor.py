# stone paper and scissor

import random

game_list = ["rock","paper","scissor"]  #ccreating list

flage = True

while flage:
    com= random.choice(game_list)
    user = input("chose rock / paper / scissor :")
    print("com enter:",com)
    if user == com:
        print("tie")
    
    elif user == "rock" and com == "scissor":
        print("user won the match")

    elif user == "rock" and com == "paper":
        print("com won the match")

    elif user == "paper" and com == "scissor":
        print("com won the match")

    elif user == "paper" and com == "rock":
        print("user won the match")

    elif user == "scissor" and com == "paper":
        print("user won the match")

    elif user == "scissor" and com == "rock":
        print("com won the match")

    else:
        print("invalid input")
        status=False


'''import random

game_list = ["rock","paper","scissor"]  #ccreating list

flage = True

while flage:
    com= random.choice(game_list)
    user = input("chose rock / paper / scissor :")
    print("com enter:",com)
    if user == com:
        print("tie")

    elif user == "rock" and com == "scissor":
        print("user won the match")

    elif user == "paper" and com == "rock":
        print("user won the match")

    elif user == "scissor" and com == "paper":
        print("user won the match")
    else:
        print("com won the match")'''