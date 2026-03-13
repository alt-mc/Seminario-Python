num = int(input("ingrese un numero: "))
multiples_of_5 = []
others_numbers = []

for i in range(1, num + 1):
    if i % 5 == 0:
        multiples_of_5.append(i)
        continue

    others_numbers.append(i)

print(f"multiplos de 5: {multiples_of_5}")
print(f"resto de los numeros: {others_numbers}")
