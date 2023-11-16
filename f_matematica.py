def soma(n1:float, n2:float):
    return n1 + n2
def subtracao(n1:float, n2:float):
    return n1 - n2
def multiplicacao(n1:float, n2:float):
    return n1 * n2
def divisao(n1:float, n2:float):
    return(n1 / n2)

while True:
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))
    calculo=str(input("Escolha a operadora: somar = 1 / subtrair = 2 / multiplicar = 3 / dividir = 4: "))
    if calculo == "1":
        print(f"O resultado é {soma(num1, num2)}")
    elif calculo == "2":
        print(f"O resultado é {subtracao(num1, num2)}")
    elif calculo == "3":
        print(f"O resultado é {multiplicacao(num1, num2)}")
    elif calculo == "4":
        if divisao(num1, num2) == 0:
            print("Erro de resultado")
        else:
            print(f"O resultado é {divisao(num1, num2)}")

    repetir = (str(input("Deseja continuar? SIM = 1, NÃO = 2: ")))
    if repetir == "2":
        break
    