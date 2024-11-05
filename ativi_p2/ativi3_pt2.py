#programa que apresenta fatorial
y=int(input("escolha um número para saber a fatorial:"))
h=y-1
for x in range(h,1,-1):
    print(x)
    y *= x
    print(y)