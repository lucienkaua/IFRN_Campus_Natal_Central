import math

a = float(input("Digite o tamanho da reta A: "))
b = float(input("Digite o tamanho da reta B: "))
c = float(input("Digite o tamanho da reta C: "))

if not (a + b >= c and a + c >= b and b + c >= a):
    print("Com esses comprimentos não é possível formar um triângulo.")
    quit()

radA = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
radB = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
radC = math.acos((b ** 2 + a ** 2 - c ** 2) / (2 * a * b))

grausA = math.degrees(radA)
grausB = math.degrees(radB)
grausC = math.degrees(radC)

# Ângulos
if grausA < 90 and grausB < 90 and grausC < 90:
    print("O triângulo é acutângulo (todos os ângulos são agudos).")
elif grausA == 90 or grausB == 90 or grausC == 90:
    print("O triângulo é retângulo (possui um ângulo reto).")
else:
    print("O triângulo é obtusângulo (possui um ângulo obtuso).")

# Lados
if a == b == c:
    print("O triângulo é equilátero (todos os lados são iguais).")
elif a == b or a == c or b == c:
    print("O triângulo é isósceles (dois lados são iguais).")
else:
    print("O triângulo é escaleno (todos os lados são diferentes).")
