from random import randint

play_game = "Y"


player_one_score = 0
player_two_score = 0
roundsPlayed = 0
maxRound = 3

def playGame():
    global play_game
    global player_one_score
    global player_two_score
    global roundsPlayed
    global maxRound

    while play_game == "Y":
        player_one_roll = randint(1, 6)
        player_two_roll = randint(1, 6)

        if player_one_roll > player_two_roll:
            print(f"player One wins with the number:  {player_one_roll}")
            player_one_score += 1
            roundsPlayed += 1
        elif player_two_roll > player_one_roll:
            print(f"player Two wins with the number:  {player_two_roll}")
            player_two_score += 1
            roundsPlayed += 1
        else:
            roundsPlayed += 1
        if player_one_score >= maxRound:
            play_game = "N"
            print(f"Game Over! Player One won! [{player_one_score}:{player_two_score}]")
        elif player_two_score >= maxRound:
            play_game = "N"
            print(f"Game Over! Player Two won! [{player_one_score}:{player_two_score}]")
        elif roundsPlayed == maxRound:
            play_game = "N"
            if player_one_score > player_two_score:
                print(f"Game Over! Player One won! [{player_one_score}:{player_two_score}]")
            elif player_two_score > player_one_score:
                print(f"Game Over! Player Two won! [{player_one_score}:{player_two_score}]")
            else:
                print(f"Nobody Wins! You both SUCK! [{player_one_score}:{player_two_score}]")
    playAgain = input("Play Again? [Y/N]: ")
    if playAgain == "Y" or playAgain == "y":
        play_game = "Y"
        
        player_one_score = 0
        player_two_score = 0
        roundsPlayed = 0
        maxRound = 3
        playGame()
    else:
        print("Thanks for Playing!")

playGame()