print("\nContador usando WHILE:")

# Laço while de 1 a 100 exibindo apenas números pares
numero = 1
while numero <= 100:
    if numero % 2 == 0:  # operador lógico para verificar se é par
        print(numero)
    numero += 1  # incrementa o contado
print("Fim do programa.")