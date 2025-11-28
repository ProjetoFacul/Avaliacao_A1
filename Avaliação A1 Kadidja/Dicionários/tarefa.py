# Dicionário que irá armazenar os produtos
# A chave será o nome do produto e o valor será o preço
produtos = {}
print("----------------------------------------------------")
print("Cadastro de produtos (digite 'sair' no nome para encerrar)")

while True:
    nome = input("Digite o nome do produto: ")

    # Condição para encerrar o cadastro
    if nome.lower() == "sair":
        break

    # Entrada do preço
    preco = float(input(f"Digite o preço de '{nome}': "))

    # Armazena no dicionário
    produtos[nome] = preco

print(" ")
print("----------------------------------------------------")
print("Produtos cadastrados:")
for nome, preco in produtos.items():
    print(f"Produto: {nome}  |  Preço: R$ {preco:.2f}")
print("----------------------------------------------------")
print("\nFim do programa.")
