#Entrada principal do sistema
#Inicia ele
#Chama funções
#Contém o escopo geral do projeto (menu)

from funcionario import (listar_funcionarios,
cadastrar_funcionario,
atualizar_cargo,
deletar_funcionario
)

while True:
    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar funcionários")
    print("2 - Cadastrar funcionário")
    print("3 - Atualizar salário")
    print("4 - Remover funcionário")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

#Listar
    if opcao == "1":
        listar_funcionarios()
#Cadastrar
    elif opcao == "2":
        nome = input("Nome: ")
        CPF = input("CPF: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: "))
        data_admissao = input("Data de admissão(AAAA-MM-DD): ")
        id_setor = int(input("ID setor: "))

        cadastrar_funcionario(nome, CPF, cargo, salario, data_admissao, id_setor)
        print("Funcionário cadastrado com sucesso!")
#Atualizar
    elif opcao == "3":
        id_funcionario = input("ID do funcionário: ")
        novo_cargo = input("Cargo: ")

        atualizar_cargo(id_funcionario, novo_cargo)
#Deletar
    elif opcao == "4":
        id_funcionario = input("ID funcionario: ")

        deletar_funcionario(id_funcionario)
#Sair
    elif opcao == "0":
        print("bye bye")
        break
    else:
        print("Tente novamente!!")