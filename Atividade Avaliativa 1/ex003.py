horaInicial = int(input("Hora da partida (h): "))
minuInicial = int(input("Minuto da partida (min): "))
horaChegada = int(input("Hora da chegada (h): "))
minuChegada = int(input("Minuto da chegada (min): "))
segDescanso = int(input("Segundos de descanso (seg): "))
litrosGasto = float(input("Litros gastos durante viagem (l): "))
valorLitros = float(input("Preço atual do litro (R$): "))
distanTotal = float(input("Quantos KM percorridos (km): "))

if horaInicial == horaChegada and minuInicial == minuChegada:
    print("Por favor digite um horário de início menor ou maior que o horário de chegada.")
    quit()

if horaInicial > horaChegada:
    tempoTotal = (24 - (horaInicial + (minuInicial / 60))) + (horaChegada + (minuChegada / 60))
else:
    tempoTotal = (horaChegada + (minuChegada / 60)) - (horaInicial + (minuInicial / 60))

# Visualização de dados
print(f"{'-' * 17} > Dados da viagem < {'-' * 17}")

# Letra A
tempoTotal *= 3600
print(f"O tempo total de viagem foi: {tempoTotal:.0f} segundos.")

# Letra B
velocidadeMedia =  distanTotal / ((tempoTotal - segDescanso) / 3600)
velocidadeMedia =  distanTotal / (tempoTotal / 3600)
print(f"Velocidade média global: {velocidadeMedia:.0f} Km/h")
print(f"Velocidade média em movimento: {velocidadeMedia:.0f} Km/h")

# Letra C
custoCombustivel = litrosGasto * valorLitros
print(f"Custo da viagem: R${custoCombustivel:.2f} Km/h")

# Letra D
kmLitro = distanTotal / litrosGasto
litroHora = litrosGasto / ((tempoTotal - segDescanso) / 3600)
realKm = custoCombustivel / distanTotal
print(f"{'-' * 20} > Desempenho < {'-' * 20}\nQuilômetro por Litro: {kmLitro} Km/l\nLitros por Hora: {litroHora} l/h\nR$ por Quilômetro: {realKm:.2f} R$/Km")