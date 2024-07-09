import random

a=input('''\nFor start press any key
For Exit Enter 0
         ''')

while(a!="0"):

    n=input('''Enter Your choice btw : S\ P\ Sc :- 
    To stop ENTER stop :- ''' )
    n=n.lower()
    list=["s","p","sc"]

    if(n=="stop"):
        break

    elif(n not in list):
        print("Invalid Choice")


        

    else:
        
        comp= random.choice([1,0,-1])

      


# comp = random.choice([1,-1,0])
        comptdict={
            1 : "Stone",
           -1 : "Paper",
            0 : "Scissor"
          }
        print(comptdict[comp])
        youdict={"s":1,
            "p":-1,
            "sc":0}
        you=youdict[n]
        print("ohk")
        
        if(comp==0 and you==0):
            print("This is tie.")
        elif(comp==0 and you==1):
            print("You Won")
        elif(comp==0 and you==-1):
            print("You Loss")

        elif(comp==1 and you==1):
            print("Tie")
        elif(comp==1 and you==-1):
            print("You Win")
        elif(comp==1 and you==0):
            print("You Loss")

            
        elif(comp==-1 and you==-1):
            print("Tie")
        elif(comp==-1 and you==1):
            print("You Loss")
        elif(comp==-1 and you==0):
            print("You Win")