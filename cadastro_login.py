from conexao_python_mysql import inserir_usuario, delete_account, buscar_usuario
from pessoa import Pessoa
import string, random, re


def validar_email(email):
    # Verifica se o email fornecido está no formato correto.

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True


def validar_senha(senha):
    # Verifica se a senha fornecida tem entre 8 e 20 caracteres.
    if len(senha) < 8 or len(senha) > 20:
        return False
    return True


def gerarCodigo():
    # Gera um código de 6 caracteres aleatórios, formados por letras maiúsculas e dígitos.
    codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return codigo


def enviarEmail(codigo, email):
    print(f"Um código foi enviado para o email {email}")
    print(f"Código: {codigo}")


def fazerCadastro():
    # Realiza o processo de cadastro de um novo usuário.
    cadastros = {}
    while True:
        nome = input("Digite o nome: ")
        if nome.strip()!="":
            break
        else:
            print("Nome inválido. Tente novamente.")

    idade = int(input("Digite a idade: "))

    while True:
        email = input("Digite o e-mail: ")
        email_exist = False
        for cadastro in cadastros.values():
            if email == cadastro.get_email():
                email_exist = True
                break
        if email_exist:
            print("Já existe um e-mail igual a este. Tente outro.")
        elif not validar_email(email):
            print("O endereço de e-mail não está no formato correto. Tente novamente.")
        else:
            break

    while True:
        senha = input("Digite uma senha: ")
        confirm_senha = input("Confirmar senha: ")
        if senha == confirm_senha:
            if not validar_senha(senha):
                print("A senha deve ter entre 8 e 20 caracteres. Tente novamente.")
            else:
                break
        else:
            print("As senhas não conferem. Tente novamente.")

    codigo = gerarCodigo()
    enviarEmail(codigo, email)

    while True:
        codigo_digitado = input("Digite o código recebido: ")
        if codigo_digitado == codigo:
            inserir_usuario(nome, email, senha, idade)
            cadastro = Pessoa(nome, email, senha, idade)
            cadastros[email] = cadastro
            print("Cadastro realizado com sucesso.")
            break
        else:
            print("Código inválido. Tente novamente")


def FazerLogin():
    # Realiza o processo de login de um usuário.
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")

    usuario = buscar_usuario(email, senha)

    if usuario:
        print("Bem-vindo,", usuario.get_nome())
    else:
        print("E-mail ou senha incorretos.")


def ExcluirConta():
    # Realiza a exclusão de um usuário.
    while True:
        email = input("Digite o e-mail: ")
        senha = input("Digite a senha: ")
        usuario = {}
        usuario = buscar_usuario(email, senha)
        if usuario:
            delete_account(email)
            del usuario
            print("Conta removida com sucesso.")
            break
        else:
            print("Falha ao remover.")


while True:
    print("1 - Fazer login")
    print("2 - Fazer Cadastro")
    print("3 - Excluir conta")

    sel_opc = input("Escolha uma opção: ")

    if sel_opc == "1":
        FazerLogin()
    elif sel_opc == "2":
        fazerCadastro()
    elif sel_opc == "3":
        ExcluirConta()
    else:
        print("Opção inválida.")
