#divisor
num = int(input("escolha um número:"))
for x in range(1, 12345678901234567890):
    if num % x == 0:
        print(f'o número {num} pode ser dividido por {x}')