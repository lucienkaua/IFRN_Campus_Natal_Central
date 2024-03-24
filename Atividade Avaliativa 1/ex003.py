horaInicial = int(input("Hora da partida (h): ")) * 3600
minuInicial = int(input("Minuto da partida (min): ")) * 60
horaChegada = int(input("Hora da chegada (h): ")) * 3600
minuChegada = int(input("Minuto da chegada (min): ")) * 60
segDescanso = int(input("Segundos de descanso (seg): "))
litrosGasto = float(input("Litros gastos durante viagem (l): "))
valorLitros = float(input("Preço atual do litro (R$): "))
distanTotal = float(input("Quantos KM percorridos (km): "))

if horaInicial > horaChegada:
    print("Por favor digite um horário de início menor que o horário de chegada.")
    quit()

# Visualização de dados
print(f"{'-' * 17} > Dados da viagem < {'-' * 17}")

# Letra A
tempo_total = (horaChegada + minuChegada) - (horaInicial + minuInicial)
print(f"O tempo total de viagem foi: {tempo_total} segundos.")

# Letra B
velocidade_media =  distanTotal / ((tempo_total - segDescanso) / 3600)
print(f"Velocidade média: {velocidade_media:.0f} Km/h")

# Letra C
custo_combustivel = litrosGasto * valorLitros
print(f"Custo da viagem: R${custo_combustivel:.2f} Km/h")

# Letra D
km_litro = distanTotal / litrosGasto
litro_hora = litrosGasto / ((tempo_total - segDescanso) / 3600)
real_km = custo_combustivel / distanTotal
print(f"{'-' * 20} > Desempenho < {'-' * 20}\nQuilômetro por Litro: {km_litro} Km/l\nLitros por Hora: {litro_hora} l/h\nR$ por Quilômetro: {real_km:.2f} R$/Km")