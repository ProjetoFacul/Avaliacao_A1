# Criando a lista vazia para armazenar os nomes
alunos = []
print("----------------------------------------------------")
print("Cadastro de alunos (digite 'sair' para encerrar)")

while True:
    nome = input("Digite o nome do aluno: ")

    # Condição para parar o cadastro
    if nome.lower() == "sair":
        break

    # Adiciona o nome na lista
    alunos.append(nome)

# Exibe todos os nomes cadastrados
print("----------------------------------------------------")
print("Lista de alunos cadastrados:")
for aluno in alunos:
    print(aluno)
print("----------------------------------------------------")
print("\nFim do programa.")
