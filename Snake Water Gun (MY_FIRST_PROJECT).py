import random

def game_win(comp , user ):
        if comp == user:
            return None
        elif comp =="S":
            if user == "W":
                    return False
            elif user == "G":
                    return True
        elif comp =="W":
            if user == "S":
                    return True
            elif user == "G":
                    return False
        elif comp =="G":
            if user == "W":
                    return True
            elif user == "S":
                    return False

       
user = input("Choose Snake(S), Water(W), or Gun(G): ")
if "S"in user:
    print(f"You choose : {user}")
    print("Computer is choosing.......")
elif "W"in user : 
    print("You choose :" , user)
    print("computer is choosing ...... ")
elif "G"in user :
    print("You choose :" , user)
    print("computer is choosing ...... ")
else :
    print("Invalid Choice")
    
    
comp = "S"

comp = random.randint(1,3)
if comp == 1 :
    comp = "S"
elif comp == 2 :
    comp = "W"
elif comp == 3 :
    comp = "G"

print (f"Computer Chooses :{comp}")
win = game_win(comp,user)
if win == None:
       print("It is a Tie")
elif win:
       print("You Win!!!!!")
else:
       print("You Loose")