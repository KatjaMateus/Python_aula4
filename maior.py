# FAÇA UMA FUNÇÃO QUE RECEBE 2 NÚMEROS E RETORNA O MAIOR DO DOIS

# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR DOIS NÚMEROS E MOSTRA NA TELA QUAL O MAIOR DOS DOIS USANDO A FUNÇÃO QUE VOCÊ ACABOU DE CRIAR

def maior(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(maior(numero1, numero2))
