notal = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (notal + nota2)/2

if media>=6.0:
    print("Você foi aprovado com média %.2f" %(media))

else:
    exame = float(input("Digite a nota do exame:"))
    novamedia = (notal + nota2+ exame)/3

if novamedia>=6.0:
    print("Você foi aprovado com nova média %.2f" (novamedia))

else:
    print("Você foi reprovado com nova média %.2f" % (novamedia))
