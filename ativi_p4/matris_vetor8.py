#
v=[]
j=[]
s=0
for s in range(0,5):
    x=input("sua idade: ")
    v.append(x)
    r=float(input("qual a sua tamanho: "))
    j.append(r)
v.reverse()
print("idades: ",v)
j.reverse()
print("tamanhos: ",j)