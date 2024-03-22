num = int(input("Insira um número inteiro entre 0 e 9999."))

if 0 <= num <= 9999:
    soma =  (num // 1000) + ((num - ((num // 1000) * 1000)) // 100) + (((num - ((num // 1000) * 1000)) - (((num - ((num // 1000) * 1000)) // 100) * 100)) // 10) + ((num - (num // 1000) * 1000) - (((num - (num // 1000) * 1000) // 100) * 100) - ((((num - ((num // 1000) * 1000)) - (((num - ((num // 1000) * 1000)) // 100) * 100)) // 10) * 10))
    print("A soma dos algarismos desse número é:", soma)

quit()