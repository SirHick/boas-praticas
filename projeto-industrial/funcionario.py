#AGORA ESTE ARQUIVO É UM MÓDULO 
#RESPONSÁVEL PELAS FUNCIONALIDADES REFERENTES A FUNCIONÁRIO


from database import conectar

#objeto
conexao = conectar()

#Chama a função, tenta estabelecer a função
#Recebe a conexao pronta
#Guarda na variavel -conexao-

if conexao.is_connected():
    #is_connected vem la da biblioteca mysql-python
    print("Banco conectado com sucesso!")

from database import conectar

#Listar funcionarios
def listar_funcionarios():
    #abrir conexao
    conexao = conectar()

    #Criar Cursor
    cursor  = conexao.cursor()

    #SQL da consulta
    sql = """
    SELECT 
        f.id_funcionario,
        f.nome,
        f.cargo,
        s.nome AS Setor
    from funcionario f
    join setor s on f.id_setor = s.id_setor
    """

    #Executa SQL
    cursor.execute(sql)

    #Recuperar dados
    dados = cursor.fetchall()

    #Exibir resultados
    for funcionario in dados:
        print(funcionario)

    #Fechar a conexão
    cursor.close()
    conexao.close()

def cadastrar_funcionario(nome, cargo, id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO funcionario
        (nome, cargo, id_setor)
        values
        (%s, %s, %s)
    """
    valores = (nome, cargo, id_setor)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Funcionário OK")

    cursor.close()
    conexao.close()

def atualizar_funcionario(cargo, id_funcionario):
    
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE funcionario
    set cargo = %s
    where id_funcionario = %s
    """
    novoValor = (cargo, id_funcionario)
    cursor.execute(sql, novoValor)
    conexao.commit()

    print("Cargo atualizado.")

    conexao = conectar()
    cursor = conexao.cursor()

def deletar_funcionario(id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()
    print("Sucesso")
    sql = """
        DELETE FROM funcionario
        WHERE id_funcionario = %s
    """

    valores = (id_funcionario,)
    cursor.execute(sql, (valores))
    conexao.commit()

    conexao = conectar()
    cursor = conexao.cursor()