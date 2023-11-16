# FAÇA UMA FUNÇÃO QUE RECEBE 2 NÚMEROS E RETORNA O MAIOR DO DOIS

# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR DOIS NÚMEROS E MOSTRA NA TELA QUAL O MAIOR DOS DOIS USANDO A FUNÇÃO QUE VOCÊ ACABOU DE CRIAR

def maior(n1:int = 10, n2:int = 5):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return "São iguais"
    
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print(f"O {maior(n1,n2)} é o maior")
print(f"O {maior()} é o maior")
print(f"O {maior(n1)} é o maior")