total = 0.0

while True:
    price = float(input("ingresa el precio del producto (0 para terminar): $"))
    if price == 0:
        break
    total += price

print(f"El total acumulado a pagar es: ${total}")
