import cards_gcis123

def deal_hand():
    Deck=cards_gcis123.make_deck()
    ShuffledDeck=cards_gcis123.shuffle(Deck)
    hand=[]
    for x in range(4):
        hand,ShuffledDeck=cards_gcis123.draw(hand,ShuffledDeck)
    return(Deck,ShuffledDeck,hand)

#"""
def test_deal_hand():
    cards_gcis123.deal(deck,4,hand1,hand2)
    assert len(hand1)==4
#"""

def discard(hand,numb):
    if len(hand)<=4:
        print("Here, No Cards were Discarded!")
    elif numb==2:
        del hand[len(hand)//2]
        del hand[len(hand)//2]
    elif numb==4:
        for x in range(4):
            del hand[-1]
    else:
        print("Here, You can only Discard 2 or 4 Cards at once!")
    return(hand)

def play_round(deck,hand):
    if len(hand)<4:
        cards_to_draw=4-len(hand)
        if len(deck)>=cards_to_draw:
            for _ in range(cards_to_draw):
                hand,deck = cards_gcis123.draw(hand,deck)
        else:
            print("\033[31mHere, Both the Deck and the Hand don't have enough Cards!\033[37m")
    
    print("\033[32mYour current hand is\033[37m:")
    for i in hand:
        cards_gcis123.print_card(i)

    if hand[0][-1]==hand[1][-1]:
        if hand[0][-1]==hand[2][-1]:
            if hand[0][-1]==hand[3][-1]:
                print("\033[30m---------------\033[37mHere, All of the Starting Cards have the Same Suit!.\n\033[31mSorry! You Lost!\033[37m")

    repeating_game=True
    while repeating_game==True:
        hand,deck,repeating_game=cards_gcis123.play_round(hand,deck)

    if len(hand)>0:
        print("\033[30m---------------\033[37m\n\033[32mYour hand is Now ->\033[37m:")
        for y in hand:
            cards_gcis123.print_card(y)
        print("\033[30m---------------\033[37m")
    else:
        print("\033[30m---------------\033[37m")
    return(hand,deck)

def main():
    #MAIN FUNCTION!
    print("\033[30m========================\n\033[32m{WELCOME TO THE GAME!}\033[37m")
    Deck,ShuffledDeck,Hand=deal_hand()
    print("\033[30m---------------\033[37m")
    Hand,FinalDeck=play_round(ShuffledDeck,Hand)
    print("\033[32m{GAME END!}\033[30m\n========================\033[37m")

main()