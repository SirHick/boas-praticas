#Conexão com o banco de dados

#instalar o drive de conexão
#MYSQLCONNECTOR
#O drive é um tradutor python --> MYSQL

import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'metalsul',
        port = 3306
)
    return conexao