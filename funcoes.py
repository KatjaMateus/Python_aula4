
  #nativas de Python

def saudacao(nome):
    print(f"Olá, {nome}, seja bem vindo")

saudacao("Abel")
saudacao("Ana")
saudacao("João")

for i in range(10):
    nome = str(input("Digite seu nome: "))
    saudacao(nome)