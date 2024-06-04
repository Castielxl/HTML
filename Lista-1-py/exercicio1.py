#E1
fValue = float(input("Digite um número: "))
sValue = float(input("Digite outro número: "))

if fValue > sValue:
    print(f"O número maior é {fValue}.")
elif sValue > fValue:
    print(f"O número maior é {sValue}")
else:
    print("Os números são iguais.")
#E2
'''fValue = float(input("Insira o primeiro valor: "))
sValue = float(input("Insira o segundo valor: "))
tValue = float(input("Insira o terceiro valor: "))

largest = max(fValue, sValue, tValue)
smaller = min(fValue, sValue, tValue)

middle = ((fValue + sValue + tValue) - (largest + smaller))
print(f"A ordem crescente é: {smaller}, {middle}, {largest}")'''
#E3
'''evenOrOdd = int(input("Digite um número: "))

if evenOrOdd % 2 == 0:
    print("Seu número é par.")
else:
    print("Seu número é ímpar")'''
#E4
'''import math
print("MENU DE OPÇÕES\n 1. Somar dois números \n 2. Raíz quadrada de um número\n\n")

choice = int(input("Escolha uma das opções acima: "))

if choice == 1:
    fValue =  float(input("Insira o primeiro valor: "))
    sValue = float(input("Insira o segundo valor: "))
    print(f"A soma de {fValue} e {sValue} é: {fValue + sValue}.")

elif choice == 2:
    value = float(input("Insira o valor para radiciação: "))
    square = math.sqrt(value)
    print(f"A raíz de {value} é: {square}")
else:
    print("Digite um dos dois números acima")'''
#E5
'''print("TABELA DE CARGOS\n 1. Escriturário\n 2. Secretário\n 3. Caixa\n 4. Gerente\n 5. Diretor\n")

choice = int(input("Escolha um dos cargos acima: "))
wage = float(input("Informe o seu salário atual: "))

if choice == 1:
    incr = 0.5
    newWage = wage + (wage * incr)
    print(f"\nSeu cargo é Escriturário. Seu salário atual é de R${wage}. você receberá um aumento de 50%. Seu novo salário é R${newWage}")
elif choice == 2:
    incr = 0.35
    newWage = wage + (wage * incr)
    print(f"\nSeu cargo é Secretário. Seu salário atual é de R${wage}. você receberá um aumento de 35%. Seu novo salário é R${newWage}")
elif choice == 3:
    incr = 0.2
    newWage = wage + (wage * incr)
    print(f"\nSeu cargo é Caixa. Seu salário atual é de R${wage}. você receberá um aumento de 20%. Seu novo salário é R${newWage}")
elif choice == 4:
    incr = 0.1
    newWage = wage + (wage * incr)
    print(f"\nSeu cargo é Gerente. Seu salário atual é de R${wage}. você receberá um aumento de 10%. Seu novo salário é R${newWage}")
elif choice == 5:
    newWage = wage
    print(f"\nSeu cargo é Diretor. Seu salário atual é de R${wage}. Você não tem aumento, otário. Seu salário continua o mesmo.")
else:
    print("Escolha uma das opções acima.")'''
#E6
'''wage = round(float(input("Digite seu salário: ")))
if wage <= 600:
    schoolAssis = 150
elif wage > 600:
    schoolAssis = 100

if wage < 501:
    incr = 0.5
    newWage = wage + schoolAssis + (wage * incr)
    print(f"Seu novo salário é de R${newWage}")
elif wage < 1201:
    incr = 0.12
    newWage = wage + schoolAssis + (wage * incr)
    print(f"Seu novo salário é de R${newWage}")
elif wage >= 1201:
    newWage = wage + schoolAssis
    print(f"Seu novo salário é de R${newWage}")'''