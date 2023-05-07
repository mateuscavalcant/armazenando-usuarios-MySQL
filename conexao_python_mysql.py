import mysql.connector
from pessoa import Pessoa
from senhas import password_mysql

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password_mysql,
    database="registros"
)


def inserir_usuario(nome, email, senha, idade):
    try:
        myCursor = mydb.cursor()

        # Adiciona um usuário novo na tabela cadastros
        sql = "INSERT INTO cadastros (Nome, Email, Senha, Idade) VALUES (%s, %s, %s, %s)"
        val = (nome, email, senha, idade)

        myCursor.execute(sql, val)

        mydb.commit()

        print(myCursor.rowcount, "record inserted.")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table:", error)


def buscar_usuario(email, senha):
    try:
        myCursor = mydb.cursor()

        # Verifica na tabela a existência de um usuário
        sql = "SELECT * FROM cadastros WHERE Email = %s AND Senha = %s"
        val = (email, senha)

        myCursor.execute(sql, val)

        result = myCursor.fetchone()

        if result:
            return Pessoa(result[0], result[1], result[2], result[3])
        else:
            return None

    except mysql.connector.Error as error:
        print("Failed to fetch data from MySQL table:", error)


def delete_account(email):
    try:
        myCursor = mydb.cursor()

        # Execute a consulta SQL para selecionar o registro com o email fornecido
        sql = "SELECT * FROM cadastros WHERE Email = %s"
        val = (email,)
        myCursor.execute(sql, val)

        # Obtenha a primeira linha do resultado (se houver)
        row = myCursor.fetchone()

        if row is not None:
            # Se a linha existir, exclua o registro
            sql = "DELETE FROM cadastros WHERE Email = %s"
            myCursor.execute(sql, val)
            mydb.commit()
            print("Conta excluída com sucesso.")
        else:
            print("E-mail não encontrado.")

    except mysql.connector.Error as error:
        print("Erro ao excluir conta:", error)
