#operadores ralacionais
#==, !=, > , <, >=, <=


#exemplo1
#print(n == 2)

#exemplo2
#print(n != 2)

#exemplo3
#n = int(input("digite o numero"))
#print(n > 3)

#exemplo4
#n = int(input("digite o numero"))
#print(n >= 3)

#exemplo5
#n = int(input("digite o numero"))
#print(n < 5)

#exemplo6
#n = int(input("digite o numero"))
#print(n <= 5)

#exemplo7
'''
x = 10
if x > 5:
    print("x > 5")
if x < 10:
    print("x < 10")
print(" fim do programa ")
'''
'''
x = 10
if x > 5:
    if x == 10:
        print("x == 10")
print("fim do programa")
'''
#exemplo8
'''
x = 10
if x < 10:
    print("x <10")
else:
    print("maior ou igual")
'''

#exemplo9
'''
x = 10
if x>5:
    print("x > 5")
if x>8:
    print("x > 8")
if x>10:
    print("x > 10")
else:
    print("else")
'''

#exemplo10
'''
#--elif
x = 10
if x>5:
    if x == 6:
        print("x == 6")
    else:
        print("x == 10")
else:
    print("else elif")
'''
#exemplo11
'''
a = 3
b = 2
if a%b ==0:
    print("par")
else:
    print("impar")
'''
#exemplo12
'''
x, y ,z = 5, 10, 8
print("x,y,z")
x, y, z
print("x,y,z")
print(x>y, x>z)
print((y - 5)==z)
'''
#exemplo13
'''
number1 = int(input("digite o numero1"))
number2 = int(input("digite o numero2"))
number3 = int(input("digite o numero3"))

largest_number = max(number1, number2, number3)
print("o maior resultado é:", largest_number)
'''
#exemplo14
'''
income = float(input("entre com os rendimentos anuais"))
if income <  85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528)* 0.32 + 14839.02
if tax <= 0:
    tax = 0.0
    tax = round(tax,0)
    print("a taxa é:",tax, "thalers")
'''
'''
#exemplo15
idade = int(input("digite a sua idade:"))
if idade >= 18:
    print(" A pessoa é maior de idade")
    print("fim do programa")
'''
#exemplo16
'''
idade = int(input("digite a sua idade:"))
if (idade >=18):
    print("a pessoa é maior de idade")
if (idade <18):
    print("a pessoa é menor de idade")
    print(" fim do programa")
'''
#exemplo17
'''
media = int(input(" digite a nota final do aluno"))
if (media >=50):
    print("o aluno foi aprovado")
else:
    print("o aluno foi reprovado")
print(" fim do programa ")
'''
#exemplo18
'''
if(nota>=9):
    print("conceito final: A")
else:
    print("o aluno foi aprovado")
'''
