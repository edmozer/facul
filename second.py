# Função para calcular o valor total do sorvete com base no sabor e quantidade de bolas
def calcular_valor_total(sabor, quantidade):
    sabor_texto = ""
    # Definindo os preços de acordo com o sabor e quantidade
    if sabor == 'tr':
        sabor_texto = "tradicional"
        if quantidade == 1:
            valor_total = 6
        elif quantidade == 2:
            valor_total = 10
        elif quantidade == 3:
            valor_total = 14
    elif sabor == 'pr':
        sabor_texto = "premium"
        if quantidade == 1:
            valor_total = 7
        elif quantidade == 2:
            valor_total = 12
        elif quantidade == 3:
            valor_total = 17
    elif sabor == 'es':
        sabor_texto = "especial"
        if quantidade == 1:
            valor_total = 8
        elif quantidade == 2:
            valor_total = 14
        elif quantidade == 3:
            valor_total = 20
    else:
        return None, None  # Retorna None se o sabor não for válido

    return valor_total, sabor_texto


# Mensagem de boas-vindas e exibição do cardápio
print("Bem-vindo a Sorveteria do Edmozer Souza Cavalcante")
print("------------------------------------------Cardapio---------------------------------")
print("| No DE BOLAS | SABOR TRADICIONAL (tr) | SABOR PREMIUM (pr) | SABOR ESPECIAL (es) |")
print("|     1       |       R$ 6,00          |       R$ 7,00      |        R$ 8,00      |")
print("|     2       |       R$ 10,00         |      R$ 12,00      |        R$ 14,00     |")
print("|     3       |       R$ 14,00         |      R$ 17,00      |        R$ 20,00     |")
print("-----------------------------------------------------------------------------------")

# Variável global para armazenar o valor total do pedido
total_pedido = 0

# Loop principal para receber os pedidos dos clientes
while True:
    # Solicitando o sabor do sorvete e a quantidade de bolas
    print("\nEntre com o sabor desejado (tr/es/pr): ")
    sabor_sorvete = input("Sabor: ")

    # Verificando se o sabor é válido
    if sabor_sorvete not in ['tr', 'pr', 'es']:
        print("Sabor de sorvete inválido! Por favor, escolha um sabor válido (tr, pr ou es).")
        continue
    print()

    # Imprimindo o sabor e solicitando a quantidade de bolas
    print(f"Entre com o sabor desejado (tr/es/pr): {sabor_sorvete.capitalize()}")

    # Solicitando a quantidade de bolas e verificando se é válida
    while True:
        quantidade_bolas = input("Entre com o numero de bolas de sorvete desejado (1/2/3): ")
        if quantidade_bolas.isdigit() and int(quantidade_bolas) in [1, 2, 3]:
            quantidade_bolas = int(quantidade_bolas)
            break
        else:
            print("Quantidade de bolas de sorvete inválida! Por favor, escolha 1, 2 ou 3 bolas.")
    print()

    # Imprimindo o sabor e a quantidade de bolas escolhidos
    print(f"Entre com o sabor desejado (tr/es/pr): {sabor_sorvete.capitalize()}")
    print(f"Entre com o numero de bolas de sorvete desejado (1/2/3): {quantidade_bolas}")

    # Calculando o valor total do pedido
    valor_total_pedido, sabor_texto = calcular_valor_total(sabor_sorvete, quantidade_bolas)

    # Verificando se o valor foi calculado corretamente
    if valor_total_pedido is None:
        print("Erro ao calcular o valor total. Por favor, tente novamente.")
        continue

    # Somando o valor do pedido atual ao valor total
    total_pedido += valor_total_pedido

    # Exibindo o valor total do pedido
    print(f"Você pediu um sorvete de sabor {sabor_texto} no valor de R${valor_total_pedido:.2f}.")


    # Perguntando se o cliente deseja fazer outro pedido
    print()
    opcao = input("Deseja pedir mais alguma coisa? (s/n): ")
    if opcao.lower() != 's':
        break
print(f"O valor total do seu pedido é R${total_pedido:.2f}.")
print("Obrigado por utilizar o app de vendas da sorveteria do Edmozer Souza Cavalcante. Volte sempre!")
