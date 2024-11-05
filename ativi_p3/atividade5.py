#celcios ou firenhent

print("conversor celcios para firenhent(e virse versa)")
print("1 - firenhent para celcios")
print("2 - celcios para firinhent")
res=int(input("escolha a unidade de medida que será convertida: "))
F_C=float(input("escolha a temperatura: "))
def C_e_F(F_C):
    if res == 1:
        C = (F_C-32)*5/9
        print("essa temperatura em celcios é: ",C)
    else:
        F = (9*F_C/5) + 32
        print("essa temperatura em firenhant é:",F)
    return
print(C_e_F(F_C))