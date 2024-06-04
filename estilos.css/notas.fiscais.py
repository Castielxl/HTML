def calculadora():
    print("Escolha uma das operações: \\n1. Adição \\n2. Subtração \\n3. Multiplicação \\n4. Divisão")
    operacao = int(input("Digite o número da operação desejada: "))

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == 1:
        resultado = num1 + num2
        print("O resultado é: ", resultado)
    elif operacao == 2:
        resultado = num1 - num2
        print("O resultado é: ", resultado)
    elif operacao == 3:
        resultado = num1 * num2
        print("O resultado é: ", resultado)
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2
            print("O resultado é: ", resultado)
        else:
            print("Não é possível dividir por zero!")
    else:
        print("Operação inválida!")

calculadora()
