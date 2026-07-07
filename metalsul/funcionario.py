from database import conectar

def listar_funcionarios():
    
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    select 
        f.id_funcionario,
        f.nome,
        f.cpf,
        f.cargo,
        f.salario,
        f.data_admissao,
        s.nome as setor
    from funcionario f
    join setor s on f.id_setor = s.id_setor
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for funcionario in dados:
        print(funcionario)

    cursor.close()
    conexao.close()

def cadastrar_funcionario(nome, cpf, cargo, salario, data_admissao, id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    insert into funcionario (nome, cpf, cargo, salario, data_admissao, id_setor)
    values (%s, %s, %s, %s, %s, %s)
    """
    valores = (nome, cpf, cargo, salario, data_admissao, id_setor)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Funcionário {nome} cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_cargo(cargo, id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()

    
    sql = """
    update funcionario
    set cargo = %s
    where id_funcionario = %s
    """
    valores = (cargo, id_funcionario)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Funcionário {id_funcionario} atualizado com sucesso!")

    cursor.close()
    conexao.close()

def deletar_funcionario(id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    delete from funcionario
    where id_funcionario = %s
    """
    valores = (id_funcionario,)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Funcionário {id_funcionario} deletado com sucesso!")

    cursor.close()
    conexao.close()