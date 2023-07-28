# Função para realizar o print de boas-vindas
def print_boas_vindas():
    print("Bem-vindo(a) ao Sistema de Gerenciamento de Pessoas!")
    print("Desenvolvido por [SEU NOME AQUI]")

# Variável global id_global com valor inicial igual a 0
id_global = 0

# Lista vazia para armazenar os colaboradores
lista_colaboradores = []

# Função para cadastrar um novo colaborador
def cadastrar_colaborador(id):
    global id_global
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))

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
                print(colaborador)
        else:
            print("Não há colaboradores cadastrados.")
    elif opcao == 2:
        id_consulta = int(input("Digite o ID do colaborador que deseja consultar: "))
        for colaborador in lista_colaboradores:
            if colaborador["id"] == id_consulta:
                print("Colaborador encontrado:")
                print(colaborador)
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
                print(colaborador)
        if not encontrados:
            print(f"Nenhum colaborador encontrado no setor '{setor_consulta}'.")
    elif opcao == 4:
        return
    else:
        print("Opção inválida.")

# Função para remover um colaborador
def remover_colaborador():
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
        print("\nMenu:")
        print("1. Cadastrar Colaborador")
        print("2. Consultar Colaborador")
        print("3. Remover Colaborador")
        print("4. Encerrar Programa")

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
