def cachorro_peso():
# Solicita ao usuário que digite o peso do cachorro em kg
  peso = input("Digite o peso do cachorro em kg: \n")

  try:
    # Converte a entrada para um valor numérico
    peso = float(peso)
  except ValueError:
    # Se ocorrer um erro ao converter, exibe uma mensagem de erro e pede que o usuário digite novamente
    print("Voce digitou um valor nao numerico. Por favor digite o peso do cachorro novamente.\n")
    return cachorro_peso()
  # Verifica a faixa de peso e retorna o valor base correspondente
  if peso < 3:
    return 40
  elif peso < 10:
    return 50
  elif peso < 30:
    return 60
  elif peso < 50:
    return 70
  else:
    # Se o peso for maior ou igual a 50, exibe uma mensagem de erro e pede que o usuário digite novamente
    print("Não aceitamos cachorros tão grandes.\nPor favor digite o peso do cachorro novamente.\n")
    return cachorro_peso()


def cachorro_pelo():
  # Solicita ao usuário que digite o tipo de pelo do cachorro
  pelo = input("Digite o tipo de pelo do cachorro: \nc - Curto \nm - Medio \nl - Longo\n")
  # Verifica a escolha do usuário e retorna o multiplicador correspondente
  if pelo.lower() == "c":
    return 1
  elif pelo.lower() == "m":
    return 1.5
  elif pelo.lower() == "l":
    return 2
  else:
    # Se o tipo de pelo for inválido, exibe uma mensagem de erro e pede que o usuário digite novamente
    print("O tipo de pelo deve ser c, m ou l.")
    return cachorro_pelo()


def cachorro_extra():

  valor_extra = 0

  while True:
    # Exibe as opções de serviços adicionais para o usuário e solicita uma escolha
    servico_extra = int(input("Deseja adicionar mais algum servico? \n1 - Cortar unhas - R$ 10,00\n2 - Escovar dentes - R$ 12,00\n3 - Limpar orelhas - R$ 15,00\n0 - Não quero mais nada \n"))

    if servico_extra == 1:
      valor_extra += 10
    elif servico_extra == 2:
      valor_extra += 12
    elif servico_extra == 3:
      valor_extra += 15
    elif servico_extra == 0:
      # Se a opção for 0, encerra o loop e retorna o valor total dos serviços adicionais
      break
    else:
      # Se a opção for inválida, exibe uma mensagem de erro e solicita que o usuário digite novamente
      print("O serviço extra deve ser 1, 2, 3 ou 0.")

  return valor_extra


def main():
  # Exibe uma mensagem de boas-vindas ao usuário
  print("Bem-vindo(a) ao petshop do Edmozer Souza Cavalcante!")

  peso = cachorro_peso()
  pelo = cachorro_pelo()
  valor_extra = cachorro_extra()

  total = peso * pelo + valor_extra

  print(f"O valor total a pagar é R${total}.(Peso: {peso} * Pelo: {pelo} + Adicional(is): {valor_extra}) ")



if __name__ == "__main__":
  main()
