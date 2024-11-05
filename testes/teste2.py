x=input("escolha um número, e falarei se é par ou impar")
def epar(x): 
    return(x % 2 == 0)

def par_ou_impar(x):
    if epar (x):
        return "par"
    else:
        return "impar"

print(par_ou_impar(x))