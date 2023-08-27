# Msg de boas vindas
def print_boas_vindas():
    print("Bem-vindo(a) ao Sistema de controle de colaboradores do Edmozer Cavalcante")

# Variável global id_global com valor inicial igual a 1 p/ que o id do primeiro colaborador cadastrado nao seja 0
id_global = 1

# Lista vazia para armazenar os colaboradores
lista_colaboradores = []

# Função para cadastrar um novo colaborador
def cadastrar_colaborador(id):
    global id_global
    print("****************************************")
    print("-----MENU CADASTRAR COLABORADOR---------")
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")

    while True:
        salario_input = input("Digite o salário do colaborador em reais: ")
        try:
            salario = float(salario_input)
            break
        except ValueError:
            print("Valor inválido para o salário. Digite um valor numérico válido.")

    colaborador = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_colaboradores.append(colaborador)
    id_global += 1

# Função para consultar os colaboradores
def consultar_colaborador():
    print("****************************************")
    print("-----MENU CONSULTAR COLABORADOR---------")
    print("Opções de consulta:")
    print("1. Consultar Todos")
    print("2. Consultar por Id")
    print("3. Consultar por Setor")
    print("4. Retornar ao menu")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        if lista_colaboradores:
            print("Lista de todos os colaboradores:")
            for colaborador in lista_colaboradores:
                print("ID:", colaborador["id"])
                print("Nome:", colaborador["nome"])
                print("Setor:", colaborador["setor"])
                print("Salário:", colaborador["salario"])
                print("--------")
        else:
            print("Não há colaboradores cadastrados.")
    elif opcao == 2:
        id_consulta = int(input("Digite o ID do colaborador que deseja consultar: "))
        for colaborador in lista_colaboradores:
            if colaborador["id"] == id_consulta:
                print("Colaborador encontrado:")
                print("ID:", colaborador["id"])
                print("Nome:", colaborador["nome"])
                print("Setor:", colaborador["setor"])
                print("Salário:", colaborador["salario"])
                break
        else:
            print("Colaborador não encontrado.")
    elif opcao == 3:
        setor_consulta = input("Digite o setor que deseja consultar: ")
        encontrados = False
        for colaborador in lista_colaboradores:
            if colaborador["setor"].lower() == setor_consulta.lower():
                if not encontrados:
                    print(f"Colaboradores do setor '{setor_consulta}':")
                    encontrados = True
                print("ID:", colaborador["id"])
                print("Nome:", colaborador["nome"])
                print("Setor:", colaborador["setor"])
                print("Salário:", colaborador["salario"])
                print("--------")
        if not encontrados:
            print(f"Nenhum colaborador encontrado no setor '{setor_consulta}'.")
    elif opcao == 4:
        return
    else:
        print("Opção inválida.")

# Função para remover um colaborador
def remover_colaborador():
    print("****************************************")
    print("-----MENU REMOVER COLABORADOR---------")
    id_remocao = int(input("Digite o ID do colaborador que deseja remover: "))
    for i, colaborador in enumerate(lista_colaboradores):
        if colaborador["id"] == id_remocao:
            del lista_colaboradores[i]
            print("Colaborador removido com sucesso.")
            return
    else:
        print("Colaborador não encontrado.")

# Função principal
def main():
    print_boas_vindas()

    while True:
        print("****************************************")
        print("\n------------MENU PRINCIPAL----------")
        print("1. Cadastrar Colaborador")
        print("2. Consultar Colaborador(es)")
        print("3. Remover Colaborador")
        print("4. Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            cadastrar_colaborador(id_global)
        elif opcao == 2:
            consultar_colaborador()
        elif opcao == 3:
            remover_colaborador()
        elif opcao == 4:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()