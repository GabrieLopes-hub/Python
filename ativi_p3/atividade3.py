#num maior
a=input("escolha um valor")
b=input("escolha outro valor")
def maior(a, b):
    if a<b:
        print(b,"é maior que ",a)
    else:
        print(a,"é maior que ",b)
    return
print(maior(a, b))