#slar
soma = 0
contador = 0
while True:
    valor = float(input("Digite um número (ou um número negativo para encerrar): "))
    if valor < 0:
        break
    else:
        soma += valor
        contador += 1
        print("Número digitado:", valor)
        if contador > 0:
            media = soma / contador
            print("Soma dos números:", soma)
            print("Média dos números:", media)