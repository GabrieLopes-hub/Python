#sla
ida21=0
ida50=0
while True:
    idade=int(input("quantos anos você tem? (-99 para sair): "))
    if idade==-99:
        break
    if idade <= 21:
        print (idade)
        ida21 += 1
        print(ida21)
    if idade >= 50:
        print(idade)
        ida50 += 1
        print(ida50)