def imc(p:float, a:float):
    return p/(a**2)

lista_imc = []
for i in range(2):
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: ")) 
    lista_imc.append(imc(peso, altura))

print(lista_imc)
