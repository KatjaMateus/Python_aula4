def hora_aula (m:float, h:float):
    return m / h

mensal = float(input("Quanto você ganha por mês? "))
hora = float(input("Quantas horas você trabalha por mês? "))


valor_hora = hora_aula(mensal, hora)
print(f"a hora aula é {valor_hora:.2f}")