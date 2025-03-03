import random

ques=("who was the first person to land on the moon?")

def check():
   loop=True
   turn = 0
   while loop:
       guess=(input("Enter your answer"))

   
   

       if guess == ques:
        print("Neil Armstrong") 
       elif guess != ques:
        print("Nope! try again!") 
       else:
        print("Your guess is correct") 
        break
     
       turn=turn+1
       print("You have taken",turn,"turns")


print("----------------------------------------------------------------------------------------------------------------")
print("Welcome to the Quiz game!!!")
print("Instructions: You have to guess 1 question right")
print("----------------------------------------------------------------------------------------------------------------")
check()
