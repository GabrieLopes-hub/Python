#
media=[]
s=0
def filtro(num):
    return num > 7
for s in range (3):
    n1=float(input("nota: "))
    n2=float(input("nota: "))
    n3=float(input("nota: "))
    n4=float(input("nota: "))
    med=(n1+n2+n3+n4)/4
    print(med)
    media.append(med)
resultado = list(filter(filtro, media))
print(resultado)