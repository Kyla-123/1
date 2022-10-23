x=float(input('Podaj x:'))
y=float(input('Podaj y:'))
print('''
1)Dodawanie
2)Odejmowanie
3)Mnożenie
4)Dzielenie
5)Potęgowanie

''')

z=int(input('Jaką operację chcesz wykonać?'))
if z>=6 or z<=0:
    print('niepoprawna wartość')
    exit()
if z==1:
    w=x+y
elif z==2:
    w=x-y
elif z==3:
    w=x*y
elif z==4:
    if y==0:
        print('niemożliwe działanie')
        exit()
    else:
         w=x/y
elif z==5:
    w=x**y
else:
    print('niepoprawna operacja')
    exit()
print(f'Wynik = {w}')