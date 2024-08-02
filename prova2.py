#Criar programa para verificação de número positivo, negativo ou zero.

numero = float(input(f"Digite um número: "))

if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero == 0:
    print(f"O número {numero} é zero.")
else:
    print(f"O número {numero} é negativo.")