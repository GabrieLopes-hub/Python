#
y=[]
s=0
for s in range(10):
    a=str(input("escolha uma letra: "))
    y.append(a)
m=y.count("b")+y.count("c")+y.count("d")+y.count("f")+y.count("g")+y.count("j")+y.count("k")+y.count("l")+y.count("m")+y.count("n")+y.count("p")+y.count("q")+y.count("r")+y.count("s")+y.count("t")+y.count("v")+y.count("w")+y.count("x")+y.count("z")+y.count("y")
print("nesta lista existem ",m,"consoantes")