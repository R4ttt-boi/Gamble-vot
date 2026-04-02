import random
import definitions as tool

start_money = float(100)
pocket = start_money
worst_case_streak = 1000
flip_outcomes = ["h", "t"]
flip_weights = [18, 20] 
loose_streak = 0

lucky_default = 'h'

high_score = 0

step = 0
max_step = -1

retirement = 1000000
try:
    while True:

    #base_bet = pocket / (2**worst_case_streak) 
        base_bet = 1

        rolled = random.choices(flip_outcomes, weights=flip_weights)
        bet = tool.revenge_bet(base_bet, loose_streak)

        if str(lucky_default) == str(rolled[0]):
            pocket += bet*2
            loose_streak = 0

        else:
            pocket -= bet
            loose_streak += 1
    

        print(f"def: {lucky_default}, roll: {str(rolled[0])}")
        print(f"pocket: {pocket} step. {step}")
    

        if pocket > high_score:
            high_score = pocket

        if pocket <= 0 or step == max_step or high_score >= retirement:
            break

        step += 1

    print(f"debt ): richest: {high_score}")
except KeyboardInterrupt:
    print(f"debt ): richest: {high_score}")

