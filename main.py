def show_card(n,args):
    
    '''Takes number of cards & list of cards as input & displays it in a user understandable manner/General card presentation'''
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
    
    card = Card((randint(1,13),randint(1,4)))
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
    
    print("\n"*10)
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
        
class BurstError(Exception):
    pass
class Wallet:

    '''Class  to keep track player wallet with its methods to win lose or tie sitaution'''

    def __init__(self):
        self.money = 5000

    def won_natural(self,bet_amount):
        self.money += 1.5 * bet_amount
        print(f"Total amount of 1.5 times of of your bet {bet_amount} INR is credited into your account.\n Now Your wallet has {self.money} INR.")

    def won(self,bet_amount):
        self.money += bet_amount
        print(f"Exact amount Equal to your bet {bet_amount} INR is credited into your wallet. \n  Now your  wallet has {self.money} INR.")
    
    def tie(self,bet_amount):

        print(f"Your bet amount is credited back into your wallet!\n Your wallet has {self.money} INR.")

    def lost(self,bet_amount):
        self.money -= bet_amount
        print(f"Dealer Will collect Your bet. \n Now You Have {self.money} INR in your in wallet. ")
        if self.money == 0:
            print("OOPS!!  You Have been lost your all Money!")
            inp = ' '
            while inp != '':
                inp = input("Press Enter To exit!")

            exit()
    def exit_game(self):

        print(f"You are levaing casinos with {self.money} INR in your wallet.")



## some declarations of properties of cards
shape = ('BLACKJACK','♠','♥','♦','♣')
symbol = ('  ','A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','Q ','K ')
value = [0,11,2,3,4,5,6,7,8,9,10,10,10,10]
player_wallet = Wallet()

## Main driver code starts here

while True:
    player_cards= [hit(),hit()]
    computer_dealer_cards = [Card((0,0)),hit(),hit()]

    print("\n"*50)


    print("***Hi! Welcome to BLACKJACK!***")
    inp = ' '
    while inp != '':
        inp = input("Press Enter to  play game:\n")
    print(f"You Have {player_wallet.money} INR in your wallet.To play You have to make a bet first.")
    bet_amount = 0
    invalid_bet_flag = False
    while bet_amount <= 0 or bet_amount > player_wallet.money :
        if invalid_bet_flag :
            print("Invalid Bet!")
        bet_amount = int(input("Enter Your Bet amount: \n "))
        invalid_bet_flag = True

    show_board()
    if computer_dealer_cards[1].symbol == 'A ' or computer_dealer_cards[1].value == 0:
        if natural_check(computer_dealer_cards):
            if natural_check(player_cards):
                print("Computer Dealer & You Both has natural !..")
                print("*** IT'S A TIE! ***")
                player_wallet.tie(bet_amount)
                if replay():
                    continue
                else:
                    player_wallet.exit_game()
                    break
            else:
                print("Computer Dealer Has a Natural!")
                print("***You Loose!***")
                
                player_wallet.lost(bet_amount)

                if replay():
                    continue
                else:
                    player_wallet.exit_game()
                    break
    if natural_check(player_cards):
        computer_dealer_cards.pop(0)
        show_board()
        print("WOW!  You Got a natural!")
        print("***You WON!***")
        
        player_wallet.won_natural(bet_amount)

        if replay():
            continue
        else:
            player_wallet.exit_game()
            break
    if burst_check(computer_dealer_cards):
        print("WOW! Dealer Burst!")
        print("***YOU WON! ***")

        player_wallet.won(bet_amount)

        if replay():
            continue
        else:
            player_wallet.exit_game()
            break


        
    try:
        while True:

            hit_or_stand = input("Press Enter to make a hit or type Stand then press Enter to take stand:\n")

            if hit_or_stand == '':
                print("Make a Hit")
                player_cards.append(hit())
                show_board()
                card = player_cards[-1]
                if card.symbol == 'A ':
                    one_or_eleven = 14
                    while one_or_eleven !=1 and one_or_eleven != 11:
                        one_or_eleven = int(input("You want to count Ace as 1 or 11: \n"))
                        card.value = one_or_eleven

                if burst_check(player_cards):
                    print("Player Burst!")
                    print("***YOU LOOSE***")
                    
                    player_wallet.lost(bet_amount)

                    raise BurstError


            elif hit_or_stand.lower() == 'stand':
                print("Take A Stand")
                for card in player_cards:
                    if card.symbol == 'A ':
                        one_or_eleven = 14
                        while one_or_eleven !=1 and one_or_eleven != 11:
                            one_or_eleven = int(input("You want to count Ace as 1 or 11: \n"))
                            card.value = one_or_eleven
                print(f"Total Value of Your Cards is : {net_value(player_cards)}\n")
                break


    ## computer Dealers turn

        while True:
            if computer_dealer_cards[0] == Card((0,0)):
                computer_dealer_cards.pop(0)
                computer_dealer_cards.append(Card((0,0)))
                show_board()

            for card in computer_dealer_cards:
                if card.symbol == 'A ':

                    if net_value(computer_dealer_cards) - card.value > 5:
                        card.value = 11
                    else:
                        computer_dealer_cards.insert(-2,hit())
                        show_board()


            while net_value(computer_dealer_cards) <= 16 and net_value(computer_dealer_cards) <= net_value(player_cards):
                computer_dealer_cards.insert(-2,hit())
                show_board()

            if burst_check(computer_dealer_cards):
                print("Dealer Burst!")
                print("***YOU WON !***")

                player_wallet.won(bet_amount)

                raise BurstError



            else:
                break

    except BurstError:
        if replay():
            continue
        else:
            player_wallet.exit_game()
            break



    if net_value(player_cards) == net_value(computer_dealer_cards):
        print("*** IT'S A TIE!***")
        player_wallet.tie(bet_amount)
    elif net_value(player_cards) > net_value(computer_dealer_cards):

        print("*** YOU WON! ***")

        player_wallet.won(bet_amount)

    else:


        print("*** YOU LOOSE ***")
        player_wallet.lost(bet_amount) 
    if replay():
        continue
    else:
        player_wallet.exit_game()
        break
