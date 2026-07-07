from database import conectar

def listar_fornecedores():
    
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    select 
        f.id_fornecedor,
        f.razao_social,
        f.cnpj,
        f.telefone,
        f.cidade,
        f.ativo
    from fornecedor AS f
    """

    cursor.execute(sql)
    dados = cursor.fetchall()


    for fornecedor in dados:
        print(fornecedor)

    cursor.close()
    conexao.close()

def cadastrar_fornecedor(razao_social, cnpj, telefone, cidade):
    
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    insert into fornecedor (razao_social, cnpj, telefone, cidade)
    values (%s, %s, %s, %s)
    """
    valores = (razao_social, cnpj, telefone, cidade)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Fornecedor {razao_social} cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_telefone(id_fornecedor, telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    update fornecedor
    set telefone = %s
    where id_fornecedor = %s
    """
    valores = (telefone, id_fornecedor)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Telefone do fornecedor {id_fornecedor} atualizado com sucesso!")

    cursor.close()
    conexao.close()

def deletar_fornecedor(id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE fornecedor
    SET ativo = 0
    where id_fornecedor = %s
    """

    valores = (id_fornecedor,)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Fornecedor {id_fornecedor} deletado com sucesso!")

    cursor.close()
    conexao.close()