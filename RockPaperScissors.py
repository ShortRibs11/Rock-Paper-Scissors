# Rock Paper Scissors Program
# Plays a game of Rock, Paper, Scissors with the user
# Winner is best 3 out of 5
# Author: Jacob "ShortRibs" Hake
    
# Import the randint function
from random import randint

# String used to simulate a cleared screen
clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

choice = -1
while choice != 0:
    # Display the main menu
    print("\tRock, Paper, Scissors")
    print()
    print("Type your selection and press Enter(or Return):")
    # Get the user's main menu selection
    choice = int(input("\t1: Play Game\t2: How to Play\t0: Exit Game\n\t\t"))

    # if the user selected play game, start the game
    if (choice == 1):
        # Start the game
        print(clear)
            
        # Points the player has won
        playerPts = 0
        # Points the CPU has won
        opposePts = 0
        
        # Play 5 rounds at most
        for x in range(5):
            
            # Initially have our player and CPU choices identical
            choice = -1
            oppose = -1
            
            # We will need to try again if there is a tie
            # Also skip any rounds after a side has won
            while ((choice == oppose) and (playerPts < 3) and (opposePts < 3)):
                
                # Get the player's choice
                print("Rock(1), Paper(2), or Scissors(3)?")
                choice = int(input("Enter your selection: "))
                # Get the CPU's choice
                oppose = randint(1,3)
            
                # If the player chose Rock
                if (choice == 1):
                    # If the CPU chose Rock
                    if (oppose == 1):
                        # It's a tie
                        print("\t\t\t\t\tYou: "+str(playerPts)+"\tHenley: "+str(opposePts))
                        print("You choose Rock! I choose Rock!\n" +
                              "Rocks are best friends: It's a tie!")
                    # If the CPU chose Paper
                    elif (oppose == 2):
                        opposePts += 1
                        print("\t\t\t\t\tYou: "+str(playerPts)+"\tHenley: "+str(opposePts))
                        print("You choose Rock! I choose Paper!\n"+
                              "Paper covers Rock: I win!")
                    # If the CPU chose Scissors
                    elif (oppose == 3):
                        playerPts += 1
                        print("\t\t\t\t\tYou: "+str(playerPts)+"\tHenley: "+str(opposePts))
                        print("You choose Rock! I choose Scissors!\n"+
                              "Rock crushes Scissors: You win!")
                # If the player chose Paper
                elif (choice == 2):
                    # If the CPU chose Rock
                    if (oppose == 1):
                        # It's a tie
                        playerPts += 1
                        print("\t\t\t\t\tYou: "+str(playerPts)+"\tHenley: "+str(opposePts))
                        print("You choose Paper! I choose Rock!\n" +
                              "Paper covers Rock: You win!")
                    # If the CPU chose Paper
                    elif (oppose == 2):
                        print("\t\t\t\t\tYou: "+str(playerPts)+"\tHenley: "+str(opposePts))
                        print("You choose Paper! I choose Paper!\n"+
                              "Papers are best friends: It's a tie!")
                    # If the CPU chose Scissors
                    elif (oppose == 3):
                        opposePts += 1
                        print("\t\t\t\t\tYou: "+str(playerPts)+"\tHenley: "+str(opposePts))
                        print("You choose Paper! I choose Scissors!\n"+
                              "Scissors cuts Paper: I win!")
                # If the player chose Scissors
                else:
                    # If the CPU chose Rock
                    if (oppose == 1):
                        # It's a tie
                        opposePts += 1
                        print("\t\t\t\t\tYou: "+str(playerPts)+"\tHenley: "+str(opposePts))
                        print("You choose Scissors! I choose Rock!\n" +
                              "Rock crushes Scissors: I win!")
                    # If the CPU chose Paper
                    elif (oppose == 2):
                        playerPts += 1
                        print("\t\t\t\t\tYou: "+str(playerPts)+"\tHenley: "+str(opposePts))
                        print("You choose Scissors! I choose Paper!\n"+
                              "Scissors cuts Paper: You win!")
                    # If the CPU chose Scissors
                    elif (oppose == 3):
                        print("\t\t\t\t\tYou: "+str(playerPts)+"\tHenley: "+str(opposePts))
                        print("You choose Scissors! I choose Scissors!\n"+
                              "Papers are best friends: It's a tie!")

                # If it was a tie, try again
                if (choice == oppose):
                    print("\nRematch!!")
                print("\n\n")
                
        # Display a game end message
        print("The grand total is:\n"+
              "You:    "+ str(playerPts) + "\n"+
              "Henley: "+ str(opposePts))
        
        # If the player won
        if (playerPts > opposePts):
            # Display a victory message
            print("You're the new champion!!")
        # If the player lost
        else:
            # Display a defeat message
            print("You've only added to Henley's unstoppable championship.")
        input("\t<ENTER to continue>")
        print(clear)
        
    elif (choice == 2):
        # If they chose how to play, play the tutorial
        print(clear)
        print("This game will pit you against Henley, our most intelligent AI,\n" +
              "in the world's most unpredictable game: Rock, Paper, Scissors!")
        print()
        print("You will play until one of you has won three out of five matches.\n"
              + "(Ties do not count)")
        input("\t<ENTER to continue>")
        print()
        print("Every round, you will each choose either Rock, Paper, or Scissors.\n"
              + "You can choose by entering 1 for Rock, 2 for Paper, or 3 for Scissors.")
        input("\t<ENTER to continue>")
        print()
        print("After both have made their selection, the winner will be determined:\n"
              + "\tRock crushes Scissors\n"
              + "\tScissors cuts Paper\n"
              + "\tPaper covers Rock\n"
              + "If both make the same selection, it is considered a tie.")
        input("\t<ENTER to continue>")
        
    # Send the user back to the main menu
    print(clear)
    # Refresh the choice variable (unless in the process of quitting)
    if (choice != 0):
        choice = -1
        
# When the user quits, display an exit message
input("Leaving Program.\n<ENTER>")
