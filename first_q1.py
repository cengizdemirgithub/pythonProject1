def calculation(x,y:int)->int:
    x=int(input("Geben Sie erste Zahl ein: "))
    y=int(input("Geben Sie zweite Zahl ein: "))
    summe=x+y
    sub=x-y
    teilen=x/y
    multi=x*y
    return print(f'summe ist {summe}, subextraktion ist {sub}, teilen ist {teilen}, multiple ist {multi}')
calculation(3,4)


