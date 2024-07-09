import random
comp = random.randint(1,100)
user=-1
guess=0
while(user!=comp):
    user=int(input("Enter Your Number"))
    if(user>comp):
        print("lower")
        guess+=1
    elif(user<comp):
        print("higher")
        guess+=1
print(f"U did in {guess}")
