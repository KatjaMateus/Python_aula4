def calcular_media(notas,quantidade):
    return notas / quantidade

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10!"
    elif media >= 7 and media < 10:
        return "Aprovado"
    else:
        return "Reprovado"

notas = []
soma = 0

while True:
    nota = float(input("Digite sua nota: "))
    if nota == 0000:
        break
    notas.append(nota)
quantas_notas = len(notas)
for nota in notas:
    soma += nota

media = calcular_media(soma, quantas_notas)
print(media)
print(verificar_situacao(media))