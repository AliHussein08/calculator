# Funções para operações básicas
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero."

# Função para executar a calculadora
def calculadora():
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    operacao = input("Digite o número da operação (1/2/3/4): ")

    if operacao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            print(f"{num1} + {num2} = {soma(num1, num2)}")
        elif operacao == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")
        elif operacao == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        elif operacao == '4':
            print(f"{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("Operação inválida. Tente novamente.")

    # Chama a função again() para perguntar se o usuário quer continuar
    again()

# Função para perguntar se o usuário quer realizar outra operação
def again():
    escolha = input("Deseja realizar outra operação? (S/N): ").lower()

    if escolha == 's':
        calculadora()
    elif escolha == 'n':
        print("Obrigado por usar a calculadora!")
    else:
        print("Entrada inválida.")
        again()

# Chama a função da calculadora pela primeira vez
calculadora()