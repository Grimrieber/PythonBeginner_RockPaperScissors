import random
import asciArt


def game_init():
    selection = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    
    computer_selection = random.randint(0,2)
    rps = ["Rock","Paper", "Scissors"]
    if selection == 0:
        hum_img = asciArt.rock
    elif selection == 1:
        hum_img = asciArt.paper
    else:
        hum_img = asciArt.scissors

    if computer_selection == 0:
        com_img = asciArt.rock
    elif selection == 1:
        com_img = asciArt.paper
    else:
        com_img = asciArt.scissors

    try: 
        # print(f"You have selected {str(rps[selection])} \n{hum_img} \nand the computer has selected {str(rps[computer_selection])}\n{com_img} \n")
        print(f"You have selected {str(rps[selection])} \n{hum_img} \n and the computer has selected {str(rps[computer_selection])} \n{com_img}")

        if selection == 0 and computer_selection == 1:
            print("You lose")
        elif selection == 0 and computer_selection == 2:
            print("You win")
        elif selection == 0 and computer_selection == 0:
            print("Draw")
        elif selection == 1 and computer_selection == 2:
            print("You lose")
        elif selection == 1 and computer_selection == 0:
            print("You win")
        elif selection == 1 and computer_selection == 1:
            print("Draw")
        elif selection == 2 and computer_selection == 0:
            print("You lose")
        elif selection == 2 and computer_selection == 1:
            print("You win")
        elif selection == 2 and computer_selection == 2:
            print("Draw")
        game_init()
    except:
        print("Not a valid option")
        game_init()

game_init()