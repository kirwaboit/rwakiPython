# the pig dice game practice pg. 133

import random

def display_rules():
    print ("Let's Play Big!")
    print ()
    print ("* See how many turns it takes you to get to 20.")
    print ("* Turn ends when you hold or roll a 1.")
    print ("* If you hold, you save all points for the turn.")
    print ()


def play_game ():
    turn = 1
    score = 0
    game_over = False
    while not game_over:
        turn, score, game_over = take_turn (turn, score, game_over)
    print ()  # remove this, it does nothing
    print ("Game over!")

def take_turn (turn, score, game_over):
    print ("Turn", turn)
    score_this_turn = 0
    turn_over = False
    while not turn_over:
        choice = input ("Roll or hold ? (r/h)?")
        if choice.lower () == "r":
            turn, score, turn_over = \
                  roll_dice (turn, score, score_this_turn)
        elif choice.lower () == "h":
            turn, score, turn_over, game_over =  \
                  hold_turn (turn, score, score_this_turn)
        else:
            print ("Invalid choice. Try again.")


def roll_dice (turn, score, score_this_turn):
    die = random.randint(1, 6)
    print ("Die:", str (die))
    if die == 1:
        score_this_turn = 0
        turn += 1
        print ("Turn over. No score. \n")
        turn_over = True
    else:
        score_this_turn += die
        turn_over = False
    return turn, score, score_this_turn, turn_over

def hold_turn (turn, score, score_this_turn):
    print ("Score for turn:", score_this_turn)
    score += score_this_turn
    print ("Total score:", score, "\n")
    turn_over = True
    game_over = False

    if score >= 20:
       print ("You finished in", turn, "turns!")
       game_over = True
       return turn, score, turn_over, game_over
    turn +=1
    return turn, score, turn_over, game_over


def main():
    display_rules()
    play_game ()
    print("called main")


# if started as the main module, call the main function
if __name__== "__main__":
    main()
    print("called main")