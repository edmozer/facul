def calcular_desconto(valor_unitario, quantidade):
    # Definindo os valores de desconto com base na quantidade
    if quantidade < 200:
        desconto = 0
    elif quantidade < 1000:
        desconto = 5
    elif quantidade < 2000:
        desconto = 10
    else:
        desconto = 15

    # Calculando o valor total sem desconto
    valor_total_sem_desconto = valor_unitario * quantidade

    # Calculando o valor total com desconto
    valor_desconto = (desconto / 100) * valor_total_sem_desconto
    valor_total_com_desconto = valor_total_sem_desconto - valor_desconto

    # Exibindo o resultado
    print("Bem-vindo ao aplicativo de vendas da Empresa X!")
    print("Seu nome: [coloque seu nome aqui]")  # Substitua "[coloque seu nome aqui]" pelo seu nome
    print("Valor unitário do produto: R$", valor_unitario)
    print("Quantidade do produto:", quantidade)
    print("Valor total sem desconto: R$", valor_total_sem_desconto)
    print(f"Você recebeu um desconto de {desconto}% por unidade!")
    print("Valor total com desconto: R$", valor_total_com_desconto)


# Recebendo os valores do usuário
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# Chamando a função para calcular e exibir os resultados
calcular_desconto(valor_unitario, quantidade)
