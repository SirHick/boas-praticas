#Entrada principal do sistema
#Inicia ele
#Chama funções
#Contém o escopo geral do projeto (menu)
'''
from funcionario import (listar_funcionarios,
cadastrar_funcionario,
atualizar_cargo,
deletar_funcionario
)
'''

from fornecedor import (listar_fornecedores,
cadastrar_fornecedor,
atualizar_telefone,
deletar_fornecedor)

while True:
    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar fornecedor(es)")
    print("2 - Cadastrar fornecedor")
    print("3 - Atualizar telefone")
    print("4 - Remover fornecedor")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

#Listar
    if opcao == "1":
        listar_fornecedores()
#Cadastrar
    elif opcao == "2":
        razao_social = input("Razão Social: ")
        cnpj = input("CNPJ: ")
        telefone = input("Telefone: ")
        cidade = input("Cidade: ")

        cadastrar_fornecedor(razao_social, cnpj, telefone, cidade)
        print("Fornecedor cadastrado com sucesso!")
#Atualizar
    elif opcao == "3":
        id_fornecedor = input("ID do fornecedor: ")
        novo_telefone = input("Telefone: ")

        atualizar_telefone(id_fornecedor, novo_telefone)
#Deletar
    elif opcao == '4': 
        id_fornecedor = int(input("Digite o ID do fornecedor que deseja remover: "))
    
        deletar_fornecedor(id_fornecedor)
#Sair
    elif opcao == "0":
        print("Bye bye")
        break
    else:
        print("Tente novamente!!")