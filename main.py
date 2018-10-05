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


