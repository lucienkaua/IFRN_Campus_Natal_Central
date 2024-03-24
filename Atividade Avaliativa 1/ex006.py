from datetime import *

sexo = str(input("Digite seu sexo (masculino/feminino): "))
dataNascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
inicioContrib = input("Data de início da contribuição (DD/MM/AAAA): ")

dataNascimento = datetime.strptime(dataNascimento, "%d/%m/%Y").date()
inicioContrib = datetime.strptime(inicioContrib, "%d/%m/%Y").date()

idadeAproximada = (datetime.today().date() - dataNascimento).days // 365
tempoAproximado = (datetime.today().date() - inicioContrib).days // 365

print(f"{'-'*20} > Dados de aposentadoria < {'-'*20}")

if sexo == "masculino" and idadeAproximada >= 65 and tempoAproximado >= 15:
    print("Você pode se aposentar por idade.")
elif sexo == "feminino" and idadeAproximada >= 62 and tempoAproximado >= 15:
    print("Você pode se aposentar por idade.")
elif sexo == "masculino" and tempoAproximado >= 35:
    print("Você pode se aposentar por tempo de contribuição.")
elif sexo == "feminino" and tempoAproximado >= 30:
    print("Você pode se aposentar por tempo de contribuição.")
else:
    if sexo == "masculino":
        # Se aposenta com 65 anos de idade e 15 de contribuição
        estimativaAposentadoria = dataNascimento.year + 65
        print(f"Você poderá se aposentar por idade em: {estimativaAposentadoria}")
    else:
        # Se aposenta com 62 anos de idade e 15 de contribuição
        estimativaAposentadoria = dataNascimento.year + 65
        print(f"Você poderá se aposentar por idade em: {estimativaAposentadoria}")

print(f"Você tem {idadeAproximada} anos e contribui há aproximadamente {tempoAproximado} anos.")