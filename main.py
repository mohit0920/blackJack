def show_card(n,args):
    
    '''Takes a class object as input & displays it in a user understandable manner/General card presentation'''
    for i in range(0,n):
        print('+','-'*13,'+','   ',sep='',end = '')
    print("\n",end = '')
    
    for i in range(0,n):
        print('|' , ' '*10 , args[i].symbol, ' ', '|','   ',sep = '',end= '')
    print("\n",end = '')
        
        
    for _ in range(0,2):
        for i in range(0,n):
            print('|',' '*13,'|','   ',sep = '',end = '')
        print("\n",end = '')
    
    for i in range(0,n):        
        if args[i].shape == 'BLACKJACK':
            print('|',' '*2, args[i].shape , ' '*2 , '|','   ',sep= '',end = '')
        else:
            print('|',' '*6, args[i].shape , ' '*6 , '|','   ',sep= '',end = '')
    print("\n",end = '')
    
    for _ in range(0,2):
        for i in range(0,n):
            print('|',' '*13,'|','   ',sep = '',end = '')
        print("\n",end = '')
    
    for i in range(0,n):
        print('|' ,' ', args[i].symbol, ' '*10, '|','   ',sep= '',end = '')
    print("\n",end = '')
    
    for i in range(0,n):
        print('+','-'*13,'+','   ',sep='',end= '')
    print("\n",end = '')



def hit():
    
    '''Genrates a new card randomly using randint fxn in python'''
    
    from random import randint
    
    card = Card((randint(1,13),randint(1,8)))
    try:

        for cards in player_cards:
            if card == cards:
                hit()

        for cards in computer_dealer_cards:
            if card == cards:
                hit()

    except NameError:
        pass

    return card


def show_deck():

    '''Takes No input shows Deck with number of cards left in deck'''

    print('+','-'*14,'+','   ',sep='',end = '\n')
    for _ in range(0,3):
        print('|',' '*14,'|','   ',sep = '',end = '\n')

    print('|',' '*5, "DECK", ' '*5 , '|','   ',sep= '',end = '\n')
    print('|',' '*3, 52-len(player_cards)-len(computer_dealer_cards)+1," CARDS" , ' '*3 , '|','   ',sep= '',end = '\n')
    for _ in range(0,3):
        print('|',' '*14,'|','   ',sep = '',end = '\n')
    print('+','-'*14,'+','   ',sep='',end = '\n')


def show_board():

    '''Takes No input & displays board means computer dealer Cards, deck , player cards'''

    print("***Computer Dealer***")
    show_card(len(computer_dealer_cards)-1,computer_dealer_cards)

    print('\n'*2)

    show_deck()

    print('\n'*2)

    print("***Your Cards***")
    show_card(len(player_cards),player_cards)


def burst_check(hand):

    '''Takes list  of cards a arguments & returns true if there is any burst or sum of value exceeds 21'''

    if net_value(hand) > 21:
        return True
    else:
        return False

def natural_check(hand):

    '''takes list of card as input and used to check naturals in game means if any of dealer or players make a sum of exact 21'''

    if net_value(hand) == 21:
        return True
    else:
        return False


def replay():

    '''Return true if player wants to replay or return false if player wants to exit'''

    while True:
        inp = input("Hit Enter to replay or type Exit to quit game:\n")
        if inp == '':
            return True
        elif inp .lower() == "exit":
            return False
        else:
            continue

def net_value(hand):

    '''Takes list of cards a argument & return the total value of cards'''

    value = 0
    for card in hand:
        value += card.value

    return value


class Card:
    
    def __init__(self,generator):
        self.symbol = symbol[generator[0]]
        self.shape = shape[generator[1]]
        self.value  = value[generator[0]]
        
    def __eq__(self,other):
        return (self.symbol == other.symbol) and (self.shape == other.shape)
        



## some declarations of properties of cards
shape = ('BLACKJACK','♠','♥','♦','♣','♤','♡','♢','♧')
symbol = ('  ','A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','Q ','K ')
value = [0,11,2,3,4,5,6,7,8,9,10,10,10,10]


## Main driver code starts here

while True:
    player_cards= [hit(),hit()]
    computer_dealer_cards = [Card((0,0)),hit(),hit()]

    print("\n"*5)


    print("***Hi! Welcome to BLACKJACK!***")
    inp = ' '
    while inp != '':
        inp = input("Press Enter to  play game:\n")

    show_board()
    if computer_dealer_cards[1].symbol == 'A ' or computer_dealer_cards[1].value == 0:
        if natural_check(computer_dealer_cards):
            if natural_check(player_cards):
                print("Computer Dealer & You Both has natural !..")
                print("*** IT'S A TIE! ***")
                if replay():
                    continue
                else:
                    break
            else:
                print("Computer Dealer Has a Natural!")
                print("***You Loose!***")

                if replay():
                    continue
                else:
                    break
    if natural_check(player_cards):
        print("WOW!  You Got a natural!")
        print("***You WON!***")

        if replay():
            continue
        else:
            break

    if burst_check(computer_dealer_cards):
        print("WOW! Dealer Burst!")
        print("***YOU WON! ***")
        if replay():
            continue
        else:
            break

        

    while True:

        hit_or_stand = input("Press Enter to make a hit or type Stand then press Enter to take stand:\n")

        if hit_or_stand == '':
            print("Make a Hit")
            player_cards.append(hit())
            show_board()
        elif hit_or_stand.lower() == 'stand':
            print("Take A Stand")
            for card in player_cards:
                if card.symbol == 'A ':
                    one_or_eleven = 14
                    while one_or_eleven !=1 and one_or_eleven != 11:
                        one_or_eleven = int(input("You want to count Ace as 1 or 11: \n"))
                        value[1] = one_or_eleven
            print(f"Total Value of Your Cards is : {net_value(player_cards)}\n")
            break


    ## computer Dealers turn

    while True:
        if computer_dealer_cards[0] == Card((0,0)):
            computer_dealer_cards.pop(0)
            show_board()

        for card in computer_dealer_cards:
            if card.symbol == 'A ':
                while True:

                    if net_value(computer_dealer_cards) - card.value > 5:
                        card.value = 11
                        break
                    else:
                        computer_dealer_cards.append(hit())
                        show_board()


        if net_value(computer_dealer_cards) < 17:
            computer_dealer_cards.append(hit())
            show_board()


        else:
            break

    if abs(21-net_value(player_cards)) == abs(21-net_value(computer_dealer_cards)):
        print("*** IT'S A TIE!***")
    elif abs(21-net_value(player_cards)) < abs(21-net_value(computer_dealer_cards)):
        print("*** YOU WON! ***")
    else:
        print("*** YOU LOOSE ***")

    if replay():
        continue
    else:
        break
