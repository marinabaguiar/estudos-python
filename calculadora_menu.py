while True:
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print("Resultado:", numero1 + numero2)
    elif opcao == "2":
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print("Resultado:", numero1 - numero2)
    elif opcao == "3":
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print("Resultado:", numero1 * numero2)
    elif opcao == "4":
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        if numero2 != 0:
            print("Resultado:", numero1 / numero2)
        else:
            print("Erro: Divisão por zero não é permitida.")
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")