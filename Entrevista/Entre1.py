
print("Bienvenido, vera la suecion de fibonacci")

limite = int(input("Ingresa el limite de la sucecion"))

a = 0
b = 1

print(a)
print(b)
for i in range(limite):
    c = a + b
    print(c)
    a = b
    b = c

