row_1 = ["ð©âð¦¯", "ðº", "ð¨âð¦¯"]
row_2 = ["ð©âð¦¼", "ðââï¸", "ð¤³"]
row_3 = ["ðââï¸", "ð§ââï¸", "ð"]
map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

inPut = int(input("Where is the Treasure\n"))
if inPut == 11:
    map[0][0] = "â"
    print("You are very close ð")

elif inPut == 12:
    map[0][1] = "â"
    print("Did you just pick!?\nYou are JOKER!!! ð¤¡")

elif inPut == 13:
    map[0][2] = "â"
    print("I am so sorry\nYou looseð­")

elif inPut == 21:
    map[1][0] = "ð¥"
    print("You just won a ð¥")
elif inPut == 22:
    map[1][1] = "â"
    print("I am so sorry\nYou looseð­")

elif inPut == 23:
    map[1][2] = "â"
    print("Shit!!! you are almost there ð¥¶") 

elif inPut == 31:
    map[2][0] = "â"
    print("You are very close ð") 
  
elif inPut == 32:
    map[2][1] = "â"
    print("You are very close ð")

else:
    map[2][2] = "â"
    print("Did you just pick!?\nYou are JOKER!!! ð¤¡")
