from database import conectar

#objeto
conexao = conectar()

#Chama a função, tenta estabelecer a função
#Recebe a conexao pronta
#Guarda na variavel -conexao-

if conexao.is_connected():
    #is_connected vem la da biblioteca mysql-python
    print("Banco conectado com sucesso!")

def listar_setores():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
        SELECT nome, localizacao 
        FROM setor
    '''

    cursor.execute(sql)

    dados = cursor.fetchall()

    for setor in dados:
        print(setor)

    conexao.close()
    cursor.close()


def cadastrar_setor(nome, localizacao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO setor
        (nome, localizacao)
        values
        (%s, %s)
    """
    valores = (nome, localizacao)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Setor novo OK")

    cursor.close()
    conexao.close()

def atualizar_setor(localizacao, id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE setor
    set localizacao = %s
    where id_setor = %s
    """
    novoValor = (localizacao, id_setor)
    cursor.execute(sql, novoValor)
    conexao.commit()

    print("Alteração de setor concluída.")

    cursor.close()
    conexao.close()

def deletar_setor(id_setor):
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = """
        DELETE FROM setor
        WHERE id_setor = %s
    """

    valores = (id_setor,)
    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()