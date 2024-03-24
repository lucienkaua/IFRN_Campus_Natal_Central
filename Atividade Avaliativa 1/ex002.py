valor = float(input("Digite um valor decimal positivo: "))

cedula_100, cedula_50, cedula_10, cedula_5, cedula_2, resto = 0, 0, 0, 0, 0, 0
moeda_100, moeda_50, moeda_25, moeda_10, moeda_5, moeda_1 = 0, 0, 0, 0, 0, 0

# Cédulas
if valor >= 100:
    cedula_100 += valor // 100
    valor -= cedula_100 * 100
    print(f"Cédulas de R$ 100: {cedula_100:.0f}")
if valor >= 50:
    cedula_50 += valor // 50
    valor -= cedula_50 * 50
    print(f"Cédulas de R$ 50: {cedula_50:.0f}")
if valor >= 10:
    cedula_10 += valor // 10
    valor -= cedula_10 * 10
    print(f"Cédulas de R$ 10 : {cedula_10:.0f}")
if valor >= 5:
    cedula_5 += valor // 5
    valor -= cedula_5 * 5
    print(f"Cédulas de R$ 5: {cedula_5:.0f}")
if valor >= 2:
    cedula_2 += valor // 2
    valor -= cedula_2 * 2
    print(f"Cédulas de R$ 2: {cedula_2:.0f}")

# Moedas
if valor >= 1:
    moeda_100 += valor // 1
    valor -= moeda_100 * 1
    print(f"Moedas R$ 1: {moeda_100:.0f}")
if valor >= 0.5:
    moeda_50 += 1
    valor -= 0.5
    print(f"Moedas R$ 0.50: {moeda_50:.0f}")
if valor >= 0.25:
    moeda_25 += 1
    valor -= 0.25
    print(f"Moedas R$ 0.25: {moeda_25:.0f}")
if valor >= 0.10:
    moeda_10 += 1
    valor -= 0.10
    print(f"Moedas R$ 0.10: {moeda_10:.0f}")
if valor >= 0.05:
    moeda_5 += 1
    valor -= 0.05
    print(f"Moedas R$ 0.05: {moeda_5:.0f}")

# Como o Python tem uma pequena imprecisão ao ler esse valor, decidi tomar essa alternativa para que o valor do print fique zerado e exato.
if valor != 0:
    valor = round(valor, ndigits=2)
    moeda_1 += 1
    valor -= 0.01
    print(f"Moedas R$ 0.01: {moeda_1:.0f}")