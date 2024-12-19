import random

print("Hello, world")

Caracterez = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

Longitud = int(input("Digita la longitud de tu contyraseña:8"))

Contraseña = ""

for i in range(Longitud):
    Contraseña = contraseña + random.choice(Caracterez)

print(Contraseña)


