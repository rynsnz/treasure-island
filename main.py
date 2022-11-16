print('''
               ,\--/,                       ,-,__
        ------{ @  @ }-------------------,-,| |_/|
    ----------|  \/  |-------------------| |`-/  |
              | )  ( |                ,-,`-'_/ _/
--------------`W-mm-W'----------------| | _/  /
                \  /                 /`-'/  _/|
                 WW                 /___/  /  |
                                    |   | /|  |
                                    |___|/ |  |
                                       |   |  |
                                       |   |  |
                                       |   |  |
                                       |   |  |
                                       |   |  |

''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

decision = input("Left (L) or Right (R)? ")

if decision != "L":
    print("You fell into a hole.\nGame Over.")
elif decision == "L":
    decision = input("Swim (S) or Wait (W)? ")
    if decision != "W":
        print("Attacked by trout.\nGame Over.")
    elif decision == "W":
        decision = input("Which door? Red (R) - Blue (B) - Yellow (Y) ")
        if decision == "R":
            print("Burned by fire.\nGame Over.")
        elif decision == "B":
            print("Eaten by beasts.\nGame Over.")
        elif decision == "Y":
            print("You Win!") 
        else: print("Game Over.")