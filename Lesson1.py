
def divisao(a, b):
    if b == 0:
        return "Erro! Não é possível dividir por zero."
    return a / b

while True:
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
    escolha = input("Digite o número da operação desejada: ")
    
    if escolha == '5':
        print("Encerrando o programa.")
        break
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if escolha == '1':
        resultado = soma(num1, num2)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
    elif escolha == '4':
        resultado = divisao(num1, num2)
    else:
        print("Opção inválida!")
        continue
    
    print(f"Resultado: {resultado}\n")
