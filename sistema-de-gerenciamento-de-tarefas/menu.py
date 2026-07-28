# Sistema de gerenciamento de tarefas (programação estruturada)

def exibir_menu():
    """ Exibir menu principal do sistema"""
    print("\n" + "=" * 30)
    print("SISTEMA DE TAREFAS")
    print("=" * 30)
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Concluir tarefa")
    print("4. Deletar tarefa")
    print("5. Sair")
    print("=" * 30)


# função para listar tarefas
def listar_tarefas(tarefas):
    """Mostra todas as tarefas"""
    print("\n --- Lista de Tarefas --- ")
    if not tarefas:
        print("Nenhuma tarefa na lista")
        return
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "concluida" if tarefa["concluida"] else "pendente"
        print(f"{indice}. [{status}] {tarefa['descricao']}")


# Função para adicionar uma tarefa
def adicionar_tarefa(tarefas):
    descricao = input("\nDigite a descricao da tarefa: ")
    if descricao:
        nova_tarefa = {"descricao": descricao, "concluida": False}
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{descricao}' adicionada com sucesso!")
    else:
        print("A descrição não pode estar vazia.")


# Função para concluir uma tarefa
def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        escolha = int(input("\nDigite o número da tarefa que deseja concluir: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha - 1]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefas inválido.")
    except ValueError:
        print("Por favor, digite um número válido! ")


# Função de excluir uma tarefa
def remover_tarefas(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        escolha = int(input("\nDigite o número da tarefa que deseja remover: "))
        if 1 <= escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha - 1)
            print(f"Tarefa removida com sucesso!")
        else:
            print("Número de tarefa inválido")

    except ValueError:
        print("Por favor, digite um número válido.")


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_tarefas(tarefas)
        elif opcao == '2':
            adicionar_tarefa(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            remover_tarefas(tarefas)
        elif opcao == '5':
            print("\nEncerrando o sistema...")
            break
        else:
            print("\nOpção Inválida. Escolha uma opção existente.")

#Ponto de partida do programa
if __name__ == "__main__":
    main()