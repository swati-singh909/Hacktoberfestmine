# Guess Game  
**Descripton**    
This is a python guess game where the user have to choose a number from 1 to 100    

- If the user guesses the correct number then he/she wins the game.    
- If the user guess a higher number then a message is displayed that he has to guess a little lower number
- If the user guess a smaller number then a message is displayed that he has to guess a little bigger number
- User will get 5 chances to guess the correct answer.  

```
import random

def guess(guessNo):
    randno=random.randint(1,100)
    chance=int(1)
    while chance<5:
         if randno==guessNo:
              print("Awesome! you win")
              print("Correct number is",randno)
              return True
         elif randno>guessNo:
            print("You are close guess little bit higher")
            guessNo=int(input())
            chance=chance+1
         else :
             print("You are close come a little bit lower")
             guessNo=int(input())
             chance=chance+1
    print("You ran out of chances")
    print("Correct number is",randno)
                        
   

print("Guess a number from 1 to 100")
guessNo=int(input())
guess(guessNo)
 
print("Play again!!")
choice=input()
while choice!="no":
    if choice=="yes":
        print("Guess a number from 1 to 100")
        guessNo=int(input())
        guess(guessNo)
        print("Play again!!")
        choice=input()
```
**Output**
>Guess a number from 1 to 100  
>5  
>You are close guess little bit higher  
>60  
>You are close come a little bit lower  
>34  
>You are close guess little bit higher  
>50  
>You are close come a little bit lower  
>40    
>You ran out of chances  
>Correct number is 41  
>Play again!!    
>no  

    

