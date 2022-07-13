from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)

def realizar_login():
    cad = input("******Já possui cadastro?****** \nDigite s para sim e n para não >:")

    if cad == 'n':
        cadastro()
        realizar_login()

    elif cad == 's':
        logar()

    else:
        print("Valor inválido!")

def cadastro():
    arq = open('registrados.txt', 'a')
    print('Olá, aqui você pode adicionar uma nova conta!')
    nome_usuario = input('Digite o nome de usuário: ')
    nonce, ciphertext, tag = encrypt(input('Digite uma senha: '))

    arq.write('{}; '.format(nome_usuario))
    arq.write('{}; '.format(nonce))
    arq.write('{}; '.format(ciphertext))
    arq.write('{}\n' .format(tag))

    print('Cadastro realizado com sucesso!\n')
    arq.close()

def logar():
    arq = open('registrados.txt', 'r')
    print('Efetue o seu login')
    login = input('Digite o seu nome de usuario: ')
    senha_usuario = input('Digite sua senha: ')

    registrados = arq.readlines()

    for linha in registrados:
        var = linha.split('; ') #separa o vetor e outros menores que estiverem ';' entre eles

        print(var[0])
        print(var[1])
        print(var[2])
        print(var[3])

        if var[0] == login:
            print("ENTROU NO 1º IF {}" .format(var[0]))
            #faz a verificacao da senha. primeiro tem que desriptografar a senha que foi lida
            plaintext = decrypt(var[1], var[2], var[3])
            print(plaintext)
            if senha_usuario == plaintext:
                print("Bem vindo, {}!".format(login))
                print("Senha Criptografada: {}".format(var[2]))
                print("Senha Desriptografada: {}".format(plaintext))
            else:
                print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')
    arq.close()

def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

if(__name__ == "__main__"):
    realizar_login()