a=int(input('podaj pierwszą liczbę'))
b=int(input('podaj drugą liczbę'))

if(a>b):
    większa=a
    mniejsza=b
else:
    większa=b
    mniejsza=a

while(mniejsza<=większa):
    if mniejsza%2 ==1:
        mniejsza += 1
        continue
    print(mniejsza, end=' ')
    mniejsza = mniejsza + 1

#
# x = -4
# while x <= 4:
#     print(f"f({x}) = {2*x**2-5*x-8}")
#     x = x+0.5
# while True:
#      x=int(input('Podaj liczbę:'))
#      if (x<0): break

