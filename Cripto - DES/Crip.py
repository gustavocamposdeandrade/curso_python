from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

def realizar_login():
    cad = input("******Já possui cadastro?****** \nDigite `s` para sim e `n` para não >:")

    if cad == 'n':
        cadastro()
        realizar_login()

    elif cad == 's':
        logar()

    else:
        print("Valor inválido!")

def cadastro():
    arq = open('registrados_aes.txt', 'a')
    print('Olá, aqui você pode adicionar uma nova conta!')
    nome_usuario = input('Digite o nome de usuário: ')
    senha_usuario = encrypt(input('Digite uma senha: '))

    arq.write('{}; '.format(nome_usuario))
    arq.write('{}\n'.format(senha_usuario))

    print('Cadastro realizado com sucesso!\n')
    arq.close()

def logar():
    arq = open('registrados_aes.txt', 'r')
    print('Efetue o seu login')
    login = input('Digite o seu nome de usuario: ')
    senha_login = input('Digite sua senha: ')

    registrados = arq.readlines()

    for linha in registrados:
        var = linha.split('; ') #separa o vetor e outros menores que estiverem ';' entre eles

        print(var[0])
        print(var[1])

        if var[0] == login:
            print("ENTROU NO 1º IF {}" .format(var[0]))
            #faz a verificacao da senha. primeiro tem que desriptografar a senha que foi lida
            plaintext = decrypt(var[1])
            print("decry {}" .format(plaintext))
            if plaintext == senha_login:
                print("Bem vindo, {}!".format(login))
                print("Senha Criptografada: {}".format(var[1]))
                print("Senha Desriptografada: {}".format(plaintext))
            else:
                print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')
    arq.close()

def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')

#  Encryption function
def encrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)
    cipher_text = cryptos.encrypt(text)
    return b2a_hex(cipher_text)

#  After decryption, remove the complemented spaces and use strip()  Remove
def decrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    cryptor = AES.new(key, mode)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rsplit('\0')

if(__name__ == "__main__"):
    realizar_login()