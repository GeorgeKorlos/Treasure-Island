print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
choice = input("You're at a cross road. Where do you want to go?"+' Type "left" or "right".\n').capitalize()
if choice == "Left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake."+' Type "wait" to wait for a boat. Type "swim" to swim across.\n').capitalize()
    if choice2 == "Wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").capitalize()
        if choice3 == "Yellow":
            print("Congratulations! You have found the treasure!")
        elif choice3 == "Red":
            print("You are teleported to hell. Game Over.")
        else:
            print("You enter a room full of beasts. Game Over.")
    else:
        print("You got eaten by sharks trying to swim. Game Over.")
else:
    print("You fell into a hole. Game OVer.")
