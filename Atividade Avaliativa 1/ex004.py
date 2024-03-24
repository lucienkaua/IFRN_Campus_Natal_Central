diaInicial = int(input("Digite o dia inicial: "))
mesInicial = int(input("Digite o mês inicial: "))
diaFinal = int(input("Digite o dia final: "))
mesFinal = int(input("Digite o mês final: "))

if mesInicial > mesFinal or (mesInicial == mesFinal and diaInicial > diaFinal):
    print("A data inicial não pode ser maior que data final.")
    quit()

# Número de dias da data inicial
diasDataInicial = 0
if mesInicial > 1:
    diasDataInicial += 31  # Janeiro
if mesInicial > 2:
    diasDataInicial += 28  # Fevereiro
if mesInicial > 3:
    diasDataInicial += 31  # Março
if mesInicial > 4:
    diasDataInicial += 30  # Abril
if mesInicial > 5:
    diasDataInicial += 31  # Maio
if mesInicial > 6:
    diasDataInicial += 30  # Junho
if mesInicial > 7:
    diasDataInicial += 31  # Julho
if mesInicial > 8:
    diasDataInicial += 31  # Agosto
if mesInicial > 9:
    diasDataInicial += 30  # Setembro
if mesInicial > 10:
    diasDataInicial += 31  # Outubro
if mesInicial > 11:
    diasDataInicial += 30  # Novembro

diasDataInicial += diaInicial

# Número de dias da data final
diasDataFinal = 0
if mesFinal > 1:
    diasDataFinal += 31  # Janeiro
if mesFinal > 2:
    diasDataFinal += 28  # Fevereiro
if mesFinal > 3:
    diasDataFinal += 31  # Março
if mesFinal > 4:
    diasDataFinal += 30  # Abril
if mesFinal > 5:
    diasDataFinal += 31  # Maio
if mesFinal > 6:
    diasDataFinal += 30  # Junho
if mesFinal > 7:
    diasDataFinal += 31  # Julho
if mesFinal > 8:
    diasDataFinal += 31  # Agosto
if mesFinal > 9:
    diasDataFinal += 30  # Setembro
if mesFinal > 10:
    diasDataFinal += 31  # Outubro
if mesFinal > 11:
    diasDataFinal += 30  # Novembro

diasDataFinal += diaFinal

diferenca_dias = diasDataFinal - diasDataInicial

print(f"{diaInicial:02} de {mesInicial:02} até {diaFinal:02} de {mesFinal:02} - {diferenca_dias} dias.")