# Deal or No Deal Game in Python 3.4.1
# Version 1 : Dated 29th September 2014
# Author: Geejayz

# ==============================
# IMPORTS
# ==============================

import random

# ==============================
# DECLARATIONS
# ==============================

box = ''
boxes = []
#open = ''

cash = [50, 100, 250, 500, 1000, 3000, 5000, 10000]
boxes = ['1','2','3','4','5','6','7','8'] # Use the range function here to allow the number of boxes to be quickly changed
random.shuffle(cash)

# ==============================
# FUNCTIONS
# ==============================

def pick_box (cash,boxes):
    box = ''
    while box not in boxes or box == 'X':
        box = input("Please choose a box to open.")
    box = int(box)
    boxes[box-1] = 'X'
    value = cash[box-1]
    cash[box-1] = 0
    print (boxes)
    print("The value in the box is: $"+ str(value))
    return box

def banker_offer (cash):
    moneyLeft = sum(cash)
    print ("The total money left in the game is $" + str(moneyLeft))
    offer = moneyLeft * 0.1
    print ("The banker makes you an offer of $" + str(offer))
    return offer
   
            
        
    
# ==============================
# MAIN PROGRAM
# ==============================

print('Welcome to \"Deal or No Deal\"')
print('Here is our box line up')
print (boxes)   # For debugging we print our box numbers
print ()        # This line to help with visual output only.

#print (cash)    # For debugging we print our box contents.

while box not in boxes:
    print('Pick a box between 1 and 8')
    box = input()

box = int(box)  # Converts the box number to an integer value
print ("The player has picked box " + str(box)) 
#print ("Box " + str(box) + " contains a value of $" + str((cash[(box-1)])))
playerBoxValue = cash[(box-1)] # stores the value of the players box for later

#Remove the chosen box from the list of boxes by replacing it with an X.
boxes[box-1] = 'X'
print ("The remaining choices are: ")
print (boxes)   # For debugging we print our box numbers


print ("Let's play deal or no deal!")

round = 1
decision = ''
banked = 0

while round <= len(boxes)-1:
    print() # This line to help with visual output only.
    print() # This line to help with visual output only.
    print("---oooOOO<<< ROUND " + str(round) + " >>>OOOooo---")
    pick_box(cash,boxes)
    offer = banker_offer(cash)
    if decision != "Y" and decision !="y":
        print ("Do you wish to deal y/n")
        decision = input()
        if decision == "Y" or decision =="y":
            banked = offer
            print("DEAL!!!")
            print("Let's play on as if you are still in live play.")
        else:
            print("No Deal!")
    round = round + 1

if banked > 0:
    print("You went home with $" + str(banked))

print("We're ready to open your box")
print("Your box contains $" + str(playerBoxValue))
print("That's our game over - thanks for playing!")



