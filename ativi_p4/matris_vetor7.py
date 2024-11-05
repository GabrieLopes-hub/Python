#
def par(sla):
    return sla % 2 == 0
def impar(sla):
    return sla % 2 != 0
V=[9, 8, 7, 12, 0, 13, 21]
P=list(filter(par, V))
I=list(filter(impar, V))
print(P)
print(I)