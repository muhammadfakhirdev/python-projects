import random
#array of moves list
move_list=["Rock" , "Paper" , "Scissor"]
user_choice=input("enter your choice : Rock ,Paper ,Scissor : ")
comp_choice=random.choice(move_list)
print(f"user choice = {user_choice} , computer choice = {comp_choice}")

if user_choice==comp_choice:
    print("result: match tied")

elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("computer win , better luck next time")
    else:
        print("superb!! , you win")


elif user_choice=="Paper":
    if comp_choice=="Scissor":
        print("computer win , better luck next time")
    else:
        print("superb!! , you win")

elif user_choice=="paper":
    if comp_choice=="Scissor":
        print("computer win , better luck next time")
    else:
        print("superb!! , you win")















