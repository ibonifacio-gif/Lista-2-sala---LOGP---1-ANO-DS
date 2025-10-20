a = int(input("Entre com o número A:"))
b = int(input("Entre com o número B:"))
c = int(input("Entre com o número C:"))

delta = (b*b) + (4*a*c)
x1 = (b-(delta**0.5))/(2*a)
x2 = (b+(delta**0.5))/(2*a)

if delta>0:
    print("As raízes são ", '%.2f' %x1, "e", '%.2f' %x2)

else:
    print("Não é possível calcular")
