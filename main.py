def ways ( coins, amount ) :
    if amount == 0:
        return 1
    if coins == [] or amount < 0:
        return 0
    c = coins [ 0 ]
    wwic = ways ( coins, amount - c )
    wwoc = ways ( coins [ 1 : ] , amount )
    return wwic + wwoc
print(ways ( [ 1 , 2 , 5 , 10 , 20 , 50 , 100 , 200 ] , 200))
#73682