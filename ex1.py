notal = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = (notal + nota2 + nota3)/3

if media>=6.0:
    print("Você foi aprovado com média %.2f" %(media))
else:
    print ("Você não foi aprovado com média %.2f" %(media))
