print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island\nYour mission is to find the Treasure.")
stage_1 = input("You are in a cross road. Where do you want to go?\nType 'left' or 'right'\n").lower()
if stage_1 == "left":
    lake = input("You have come to a lake.\nThere is an Island in the midlle of the lake.\nType 'wait' to wait for a boat\nType 'swim' to swim across.\n").lower()
    if lake == "wait":
        arrive = input("You have arrive at the Island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and blue. Which color do you choose?\n").lower()
        if arrive == "yellow":
            print("You have found the Treasure!!!")
        else:
            print("You lose! Game Over")
    else:
        print("You lose! Game Over")
else:
    print("You lose! Game Over")
