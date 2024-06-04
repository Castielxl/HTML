valordecompra = float(input("digite o valor de compra:"))
porcentagem = float(input("digite o valor da porcentagem:"))

porcentagem = porcentagem / 100
precofinal = valordecompra * porcentagem
print(f"o valor do comsumidor final sera de: {precofinal+valordecompra}")