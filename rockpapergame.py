import random
print("Hello welcome,")
playing=True
while playing:
    print("choose rock or \n paper or scissor for this game")
    userselect=input("write rock,paper or scissor:").lower()
    choices=["rock","paper","scissor"]
    if userselect  not in choices:
        print("you are putting an invalid character plese write rock paper or scissor")
    else:
     computerchoice=random.choice(choices)
    print(f"Computer choose:{computerchoice}")
    if userselect== computerchoice:
      print("Its a tie")
    elif userselect=="rock" and computerchoice=="scissor":
     print("you win")
    elif userselect=="rock" and computerchoice=="paper":
     print("you lose")
    elif userselect=="paper" and computerchoice=="scissor":
     print("you lose")
    elif userselect=="paper" and computerchoice=="rock":
     print("you win")
    elif userselect=="scissor" and computerchoice=="rock":
     print("you lose")
    elif userselect=="scissor" and computerchoice=="paper":
     print("you win ")
    else:
     print("there is a error")
    playoncemore=input("write yes or no for playing again:").lower()
    if not playoncemore=="yes":
     print("thnks for playing")
     playing=False
    



    






