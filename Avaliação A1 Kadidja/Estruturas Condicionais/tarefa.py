# Entrada de dados: o usuário informa sua idade
print("-------------------------------------------")
idade = int(input("Digite sua idade: "))
print("-------------------------------------------")

# Estrutura condicional para verificar autorização
if idade >= 18:
    print("Entrada permitida! Você é maior de idade.")
elif idade >= 16:
    print("Entrada permitida somente com acompanhamento de um responsável.")
else:
    print("Entrada negada. Você é menor de 16 anos.")

# Fim do programa
print("Obrigado por utilizar o sistema de verificação de idade.")
print("-------------------------------------------")
