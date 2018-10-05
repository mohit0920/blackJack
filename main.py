def show_card(n,*args):
    
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
    
    for cards in player_cards:
        if card == cards:
            hit()

    for cards in computer_dealer_cards:
        if card == cards:
            hit()

    return card


