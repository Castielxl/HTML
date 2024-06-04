custodefab = float(input("valor de fabrica:"))
imposto = float(input("valor do imposto:"))
comissao = float(input("valor da comissao:"))

valImposto = imposto / 100
valComissao = comissao / 100
custoimposto = custodefab * valImposto

print(f"o lucro do distribuidor é de R$:{(custodefab * valComissao)}. O valor do imposto é de R$: {valImposto * custodefab}. o valor final é R${(custodefab * valComissao)+ custoimposto + custodefab}")
