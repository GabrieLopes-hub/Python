"""
pessoa e senha
"""
usuario="alguem"
senha="1234"
usuario2="sla"
senha2="1234"
while True:
    print("======================")
    print("1 - entrar")
    print("2 - cadastre-se")
    print("3 - Sair")
    print("======================")
    alg=str(input("escolha uma das opções:"))
    if alg == "1":
        print("======================")
        print("colque o nome do usuario")
        pessoa=str(input("NOME:"))
        sem=str(input("SENHA:"))
        if ((usuario==pessoa) and (senha==sem)) or ((usuario2==pessoa) and (senha2==sem)):
            print("você entrou com sucesso")
            True
        else:
            print("======================")
            print("algo deu errado")
            False
    if alg == "2":
        print("======================")
        print("--depois disso você será direcionado para a tela inicial--")
        usuario2=input("coloque um novo usuario:")
        senha2=input("coloque uma nova senha:")
        False
    if alg == "3":
        break
    if alg != "1" or "2" or "3":
        print("tente denovo")
        False

