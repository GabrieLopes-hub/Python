#conceito da média final
media=float(input("qual a sua média final: "))
def conceito(media):
    if media <= 4.9:
        print("você tirou | D |")
    if (media > 4.9 and media <6.9):
        print("você tirou | C |")
    if  media > 6.9 and media < 8.9 :
        print("você tirou | B |")
    if media >= 9.0:
        print("você tirou | A |")
    return
print(conceito(media))