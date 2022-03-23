import random
#----------Pictures----------
Rock_pic = "🪨"
Paper_pic = "📰"
Scissors_pic = "✂️"
Lizard_pic = "🦎"
Spock_pic = "🖖"
#----------Pictures----------

print("Wellcome to Rock Paper Scissors Lizard Spock :)")

user_choice = int(input("Please choose one:\n0 - Rock\n1 - Paper\n2 - Scissors\n3 - Lizard\n4 - Spock\nYour Choice: "))
pc_choice = random.randint(0,4)
items = ["Rock","Paper","Scissors","Lizard","Spock"]


#----------Prevent Out Of Range----------
if user_choice > 4 or user_choice < 0:
    print("Wrong Input!!! You Lost! :(")
else:
#----------Draw Situation----------
    if user_choice == pc_choice:
        print("-------ITS\'s A DRAW!-------")
#----------User chose Rock----------
    elif user_choice == 0 and pc_choice == 1:
        print(f"You chose: {items[0]}")
        print(Rock_pic)
        print(f"Computer chose: {items[1]}")
        print(Paper_pic)
        print("-------YOU LOST!-------")
    elif user_choice == 0 and pc_choice == 2:
        print(f"You chose: {items[0]}")
        print(Rock_pic)
        print(f"Computer chose: {items[2]}")
        print(Scissors_pic)
        print("-------YOU WON!-------")
    elif user_choice == 0 and pc_choice == 3:
        print(f"You chose: {items[0]}")
        print(Rock_pic)
        print(f"Computer chose: {items[3]}")
        print(Lizard_pic)
        print("-------YOU WON!-------")
    elif user_choice == 0 and pc_choice == 4:
        print(f"You chose: {items[0]}")
        print(Rock_pic)
        print(f"Computer chose: {items[4]}")
        print(Spock_pic)
        print("-------YOU LOST!-------")
#----------User chose Paper----------
    elif user_choice == 1 and pc_choice == 0:
        print(f"You chose: {items[1]}")
        print(Paper_pic)
        print(f"Computer chose: {items[0]}")
        print(Rock_pic)
        print("-------YOU WON!-------")
    elif user_choice == 1 and pc_choice == 2:
        print(f"You chose: {items[1]}")
        print(Paper_pic)
        print(f"Computer chose: {items[2]}")
        print(Scissors_pic)
        print("-------YOU LOST!-------")
    elif user_choice == 1 and pc_choice == 3:
        print(f"You chose: {items[1]}")
        print(Paper_pic)
        print(f"Computer chose: {items[3]}")
        print(Lizard_pic)
        print("-------YOU LOST!-------")
    elif user_choice == 1 and pc_choice == 4:
        print(f"You chose: {items[1]}")
        print(Paper_pic)
        print(f"Computer chose: {items[4]}")
        print(Spock_pic)
        print("-------YOU WON!-------")
#----------User chose Scissors----------
    elif user_choice == 2 and pc_choice == 0:
        print(f"You chose: {items[2]}")
        print(Scissors_pic)
        print(f"Computer chose: {items[0]}")
        print(Rock_pic)
        print("-------YOU LOST!-------")
    elif user_choice == 2 and pc_choice == 1:
        print(f"You chose: {items[2]}")
        print(Scissors_pic)
        print(f"Computer chose: {items[1]}")
        print(Paper_pic)
        print("-------YOU WON!-------")
    elif user_choice == 2 and pc_choice == 3:
        print(f"You chose: {items[2]}")
        print(Scissors_pic)
        print(f"Computer chose: {items[3]}")
        print(Lizard_pic)
        print("-------YOU WON!-------")
    elif user_choice == 2 and pc_choice == 4:
        print(f"You chose: {items[2]}")
        print(Scissors_pic)
        print(f"Computer chose: {items[4]}")
        print(Spock_pic)
        print("-------YOU WON!-------")
    #----------User chose Lizard----------
    elif user_choice == 3 and pc_choice == 0:
        print(f"You chose: {items[3]}")
        print(Lizard_pic)
        print(f"Computer chose: {items[0]}")
        print(Rock_pic)
        print("-------YOU LOST!-------")
    elif user_choice == 3 and pc_choice == 1:
        print(f"You chose: {items[3]}")
        print(Lizard_pic)
        print(f"Computer chose: {items[1]}")
        print(Paper_pic)
        print("-------YOU WON!-------")
    elif user_choice == 3 and pc_choice == 2:
        print(f"You chose: {items[3]}")
        print(Lizard_pic)
        print(f"Computer chose: {items[2]}")
        print(Scissors_pic)
        print("-------YOU LOST!-------")
    elif user_choice == 3 and pc_choice == 4:
        print(f"You chose: {items[3]}")
        print(Lizard_pic)
        print(f"Computer chose: {items[4]}")
        print(Spock_pic)
        print("-------YOU WON!-------")
    #----------User chose Spock----------
    elif user_choice == 4 and pc_choice == 0:
        print(f"You chose: {items[4]}")
        print(Spock_pic)
        print(f"Computer chose: {items[0]}")
        print(Rock_pic)
        print("-------YOU WON!-------")
    elif user_choice == 4 and pc_choice == 1:
        print(f"You chose: {items[4]}")
        print(Spock_pic)
        print(f"Computer chose: {items[1]}")
        print(Paper_pic)
        print("-------YOU LOST!-------")
    elif user_choice == 4 and pc_choice == 2:
        print(f"You chose: {items[4]}")
        print(Spock_pic)
        print(f"Computer chose: {items[2]}")
        print(Scissors_pic)
        print("-------YOU WON!-------")
    elif user_choice == 4 and pc_choice == 3:
        print(f"You chose: {items[4]}")
        print(Spock_pic)
        print(f"Computer chose: {items[3]}")
        print(Lizard_pic)
        print("-------YOU Lizard!-------")
