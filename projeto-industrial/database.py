#Conexão com o banco de dados

#instalar o drive de conexão
#MYSQLCONNECTOR
#O drive é um tradutor python --> MYSQL

import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        #O drive tenta abrir uma conexão
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = "projetoindustrial",
        port = 3306
)
    return conexao