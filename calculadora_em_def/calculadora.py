#calculadora
def soma(n1, n2):
    return(n1+n2)
def sub(n1, n2):
    return(n1-n2)
def mult(n1, n2):
    return(n1*n2)
def div(n1, n2):
        return(n1/n2)
while True:
    print("=================================")
    print("calculadora zika")
    n1=float(input("escolha um número: "))
    n2=float(input("escolha outro número: "))
    print("=================================")
    print("+  ||  -  ||  *  ||  /")
    op=input("escolha uma operação: ")
    if op == "+":
        print(soma(n1, n2))
        r=str(input("se quiser sair digite X: "))
        if r == "X" or "x":
             break
    elif op=="-":
        print(sub(n1, n2))
        r=str(input("se quiser sair digite X: "))
        if r == "X" or "x":
            break
    elif op =="*":
        print(mult(n1, n2))
        r=str(input("se quiser sair digite X: "))
        if r == "X" or "x":
            break
    elif op == "/":
        if n1==0 or n2==0:
            print("não é possivel dividir por zero")
            r=str(input("se quiser sair digite X: "))
            if r == "X" or "x":
                break
        else:
            print(div(n1, n2))
            r=str(input("se quiser sair digite X: "))
            if r == "X":
                 break
    else:
        print("operação invalida")