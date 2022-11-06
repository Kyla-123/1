#lista_zakupów=['masło','chleb','banan','pasztet']
#print(lista_zakupów)
#print(lista_zakupów[0]+","+lista_zakupów[1])
#lista_zakupów[2]='mleko'
#print(lista_zakupów)
#print(lista_zakupów[-2]+","+lista_zakupów[-1])
import random
x=int(input('podaj liczbę elementów'))
lista1=[]
for i in range(x):
    n=random.randint(1,10)
    lista1.append(n)
print(lista1)

x1=int(input('podaj liczbę elementów dla drugiej listy'))
lista2=[]
for i in range(x):
    n=random.randint(5,15)
    lista2.append(n)
print(lista2)

x2=int(input('podaj liczbę której szukasz'))
if x2 in lista1:
    print('liczba występuje w: lista1')
elif x2 in lista2:
    print('liczba występuje w: lista2')
else:
    print("nie takiej liczby w obu zestawach")

lista_1_2=lista1+lista2
lista_1_2.sort()
print(lista_1_2)

