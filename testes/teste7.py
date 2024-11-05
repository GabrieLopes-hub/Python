#teste
f="     Olá mundo, eu sei que sou uma maquina      "
print(f.upper().startswith("Olá"))
print(f.lower().startswith("Olá"))
print(f.lower().endswith("mundo"))

print("Olá" in f)

print("falso" not in f)

print(f.count("m"))

print(f.replace("maquina","lavanderia"))

print(f)

print(f.strip)