numeros = [15, 42, 8, 91, 33]
maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
print("o maior número da lista é:", maior)