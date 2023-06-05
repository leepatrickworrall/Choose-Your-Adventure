import time

while True:
    user_name = input("What is your name?: ")
    print("\n", user_name + ", welcome to your very own adventure.")

    answer = input("\nYou find yourself within a dark alley, unaware of your "
                   "surroundings or how you managed to get here.\n"
                   "\nHow do you wish to proceed?"
                   "\n1: Remain where you are and get into a ball and cry."
                   "\n2: Proceed onwards."
                   "\n3: Call for help.\n")

    if answer == "1":
        print("\n You are eventually found.\n")
        time.sleep(0.75)
        print("However, you are found by those which find it profitable to sell"
              "your organs to fund their mayonnaise addiction, and they refuse"
              "to share any with yourself.")


    elif answer == "2":
        print("\n You found a window connecting to what is seemingly an "
              "abandoned building.\n")
        answer2 = input("What do you choose to do?\n"
                        "\n1: Check to see if the window is open."
                        "\n2: Break it open with your fist.\n")

        if answer2 == "1":
            print("The window was open. That was a lucky one.")

        else:
            print("\nYou're bleeding now.\n"
                  "\nYou really were that dumb to not check to see if it was "
                  "open first?")

    elif answer == "3":
        print("\nYou just sound pathetic. I think that I would rather be "
              "lost.\n")

    else:
        print("Not a valid option. You have lost.")