
def revenge_bet(base_bet, loose_streak):

    bet = base_bet * (2**loose_streak)

    print(f"should bet {bet}")
    
    return bet