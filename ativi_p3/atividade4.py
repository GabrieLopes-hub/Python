#num menor
a=input("escolha um valor")
b=input("escolha outro valor")
def maior(a, b):
    if a<b:
        print(a,"é menor que ",b)
    else:
        print(b,"é menor que ",a)
    return
print(maior(a, b))