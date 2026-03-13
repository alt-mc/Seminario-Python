num = int(input("ingresa un numero: "))
print(f"tabla de multiplicar del numero {num}")

for i in range(1, 10):
    res = num * i
    print(f"{num} x {i} = {res}")
