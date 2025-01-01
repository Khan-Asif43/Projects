import random
n=random.randint(1,100)
guess=0
a=-1
while (a !=n):
 a=int(input("Guess a number 1 to 100:"))
 if n==a:
    guess +=1
    print("you guessed the right number")
 elif n>a:
   guess +=1
   print("higher number please")
 elif n<a:
   guess +=1
   print("lower number please")
  
   
print(f"you guessed the number{n} in attempt {guess}")
