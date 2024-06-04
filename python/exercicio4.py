vendedor = input("digite o nome do vendedor:")
salario = float(input("digite o salario:"))
totalvendapmes = float(input("digite as vendas:"))

comissao = totalvendapmes * 0.15

print(f"o nome do vendedor é {vendedor} seu salario fixo é {salario} e a comissao é {comissao + salario}")