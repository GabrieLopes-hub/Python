"""
números digitados
"""
while True:
    sla=int(input("escolha algum número:"))
    if sla<0:
        print("este número é negativo, eu não irei contar os algarismos dele")
        break
    else:
        alg=len (str(sla))
        print("o número a seguir tem:", alg,"algarimos")