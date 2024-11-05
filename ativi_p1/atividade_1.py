"""
triplo dos números
"""
while True:
    num = int(input("Digite um número (digite 999 para sair): "))
    if num == 999:
        break
    print("O triplo de", num, "é", num * 3)