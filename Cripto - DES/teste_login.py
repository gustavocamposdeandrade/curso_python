
def login():
    cad = input("******Já possui cadastro?****** \nDigite s para sim e n para não >:")

    if cad == 'n':
        cadastro()
        login()

    elif cad == 's':
        logar()


def cadastro():
    arq = open('registrados-teste.txt', 'a')
    print('Olá, aqui você pode adicionar uma nova conta!')
    nome_usuario = input('Digite o nome de usuário: ')
    senha_usuario = input('Digite uma senha: ')
    lista = [nome_usuario, senha_usuario]
    arq.write('{} \n'.format(lista))

    print('Cadastro realizado com sucesso!\n')
    arq.close()

def logar():
    arq = open('registrados-teste.txt')
    print('Efetue o seu login')
    login = input('Digite o seu nome de usuario: ')
    senha_login = input('Digite sua senha: ')

    se_l=login.strip(',')

    registrados = arq.readlines()

    for login in registrados:
        if login in registrados[0]:
            if senha_login in login:
                print("Bem vindo, {}!".format(se_l))
                print("Senha é: {}".format(senha_login))
            else:
                print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')
    arq.close()

if(__name__ == "__main__"):
    login()