a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))

if a%6==0 and b%6==0 and c%6==0: 
    print(a, b, c, "são divisíveis por 2 e 3") 
elif a%6==0 and b%6==0 and c%6!=0:
    print(a, b, "são divisíveis por 2 e 3") 

elif a%6==0 and b%6!=0 and c%6==0:
    print(a, c, "são divisíveis por 2 e 3")

elif a%6!=0 and b%6==0 and c%6==0:
    print(b, c, "são divisíveis por 2 e 3")

elif a%6==0 and b%6!=0 and c%6!=0:
    print(a, "é divisível por 2 e 3") 

elif a%6!=0 and b%6==0 and c%6!=0:
    print(b, "é divisível por 2 e 3")

elif a%6!=0 and b%6!=0 and c%6==0: 
    print(c, "é divisivel por 2 e 3")
    
else:
    print ("Nenhum dos números é divisível por 2 e 3")
