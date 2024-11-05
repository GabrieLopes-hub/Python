#vetor de 10 números reais e mostre-os na ordem inversa.
y=[]
for a in range(10):
    n=float(input("escolha um número: "))
    y.append(n)
y.reverse()
print(y)
