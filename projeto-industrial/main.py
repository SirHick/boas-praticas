#Entrada principal do sistema
#Inicia ele
#Chama funções
#Contém o escopo geral do projeto (menu)

'''
from funcionario import listar_funcionarios
listar_funcionarios()

from funcionario import cadastrar_funcionario

cadastrar_funcionario(
    'Dabura',
    'Bruxo',
   2
)


from funcionario import atualizar_funcionario

atualizar_funcionario(
    'mago',
    3
)

from funcionario import deletar_funcionario

deletar_funcionario(2)
'''

from setor import listar_setores
from setor import cadastrar_setor
from setor import atualizar_setor
from setor import deletar_setor

listar_setores()
cadastrar_setor('Almoxarifado', 'Oeste', '45')
atualizar_setor('Norte', 2)
deletar_setor(3)