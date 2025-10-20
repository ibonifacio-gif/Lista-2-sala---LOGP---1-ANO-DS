a = int(input("Digite o primeiro lado:"))
b = int(input("Digite o segundo lado:"))
c = int(input("Digite o terceiro lado:"))

if a<b+c or b<a+c or c<b+a:
    if a==b and b==c:
        print("É um triângulo equilátero")

    elif a==b or a==c or b==c:
        print("É um triângulo isósceles")

    else:
        print("É um triângulo escaleno")

if a>b+c or b>a+c or c>b+a:
    print("Não é um triângulo")
