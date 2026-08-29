contador = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        print(numero)
        contador = contador + 1
print("Total de números pares:", contador)