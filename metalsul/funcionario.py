from database import conectar

def listar_funcionarios():
    #abrir conexão
    conexao = conectar()

    #criar cursor
    cursor = conexao.cursor()

    #sql da consulta
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

    #executa sql
    cursor.execute(sql)

    #recuperar dados
    dados = cursor.fetchall()

    #exibir dados
    for funcionario in dados:
        print(funcionario)

    #fechar a conexão
    cursor.close()
    conexao.close()

def cadastrar_funcionario(nome, cpf, cargo, salario, data_admissao, id_setor):
    #abrir conexão
    conexao = conectar()

    #criar cursor
    cursor = conexao.cursor()

    #sql de inserção
    sql = """
    insert into funcionario (nome, cpf, cargo, salario, data_admissao, id_setor)
    values (%s, %s, %s, %s, %s, %s)
    """

    #valores a serem inseridos
    valores = (nome, cpf, cargo, salario, data_admissao, id_setor)

    #executa sql
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Funcionário {nome} cadastrado com sucesso!")

    #fechar a conexão
    cursor.close()
    conexao.close()

def atualizar_cargo(cargo, id_funcionario):
    #abrir conexão
    conexao = conectar()

    #criar cursor
    cursor = conexao.cursor()

    #sql de atualização
    sql = """
    update funcionario
    set cargo = %s,
    where id_funcionario = %s
    """

    #valores a serem atualizados
    valores = (cargo, id_funcionario)

    #executa sql
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Funcionário {id_funcionario} atualizado com sucesso!")

    #fechar a conexão
    cursor.close()
    conexao.close()

def deletar_funcionario(id_funcionario):
    #abrir conexão
    conexao = conectar()

    #criar cursor
    cursor = conexao.cursor()

    #sql de exclusão
    sql = """
    delete from funcionario
    where id_funcionario = %s
    """

    #valores a serem excluídos
    valores = (id_funcionario,)

    #executa sql
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Funcionário {id_funcionario} deletado com sucesso!")