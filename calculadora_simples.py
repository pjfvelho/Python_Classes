# Função para realizar a adição
def adicao(a, b):
    return a + b

# Função para realizar a subtração
def subtracao(a, b):
    return a - b

# Função para realizar a multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a divisão
def divisao(a, b):
    if b == 0:
        return "Erro! Não é possível dividir por zero."
    return a / b

# Função principal da calculadora
def calculadora():
    while True:
        print("Opções:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        escolha = input("Escolha a operação desejada (1/2/3/4/5): ")
        
        if escolha == '5':
            print("Calculadora encerrada.")
            break
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == '1':
            resultado = adicao(num1, num2)
            print(f"Resultado: {resultado}")
        elif escolha == '2':
            resultado = subtracao(num1, num2)
            print(f"Resultado: {resultado}")
        elif escolha == '3':
            resultado = multiplicacao(num1, num2)
            print(f"Resultado: {resultado}")
        elif escolha == '4':
            resultado = divisao(num1, num2)
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida! Tente novamente.")

# Chame a função da calculadora para iniciar o programa
calculadora()
