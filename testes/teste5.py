a=5

def muda_e_imptime():
    global a
    a=7
    print("a dentro da função: %d" % a)
print("a antes de mudar: %d" % a)
muda_e_imptime()
print("a depois de mudar: %d" % a)