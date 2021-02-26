from random import randint

# Execução do menu
def menu():

    opcao = int(input('Olá, mundo!\n\nSelecione uma das opções a seguir:\n1 - Definir conjunto de chaves\n2 - Sair do programa\n'))

    if opcao == 1:      
        gerar_chaves()
    elif opcao == 2:
        print('\nObrigado por usar nosso programa!\n\nDesenvolvido por:\nAdriano Mello\nGustavo Lourenço\nLucas Rangel\nMatheus Oliveira\nNicolas Bianchi\n')
    else:
        print('\nValor inválido.\n\n')
        menu()

# Gera as chaves necessárias para a criptografia
def gerar_chaves():

    p = int(input('Insira um número primo para P: '))
    q = int(input('Insira um número primo para Q: '))

    if numero_primo(p) and numero_primo(q):
        global n, funcao_phi, e, d

        n = p * q
        funcao_phi = (p - 1) * (q - 1)
        e = verificador()
        d = pow(e, -1, funcao_phi)
        print(f'\nChaves públicas:\nN = {n}\nE = {e}\nChaves privadas:\nP = {p}\nQ = {q}\nD = {d}\n')
    else:
        print('Valores inválidos! É necessário informar apenas números ímpares.\n\n')
        gerar_chaves()
    
    print('Chaves geradas com sucesso.')
    cripto_mensagem()      

# Verificador de número primo
def numero_primo(valor):

    contador = 0
    resultado = False
    
    for i in range(1, valor + 1):
        if valor % i == 0:
            contador += 1
    
    if contador == 2:
        resultado = True
    
    return resultado

# Máximo divisor comum
def mdc(a, b):

    e = a

    while a != 0:
        a, b = b % a, a

    valores = [b, e]

    return valores

# Gera e verifica o número que irá para a variável 'e'
def verificador():
    
    b = mdc(randint(1, funcao_phi - 1), funcao_phi)

    if b[0] != 1:
        while b[0] != 1:
            b = mdc(randint(1, funcao_phi - 1), funcao_phi)
    
    return b[1]

# Função matemática para criptografar mensagem
def encripta(m, e, n):

    c = (m ** e) % n

    return c

# Função matemática para ddescriptografar mensagem
def descript(c, d, n):

    m = (c ** d) % n

    return m

# Criptografa a mensagem
def cripto_mensagem():

    global mensagem_final, mensagem

    opcao = int(input('\n\nSelecione uma das opções a seguir:\n1 - Criptografar mensagem\n2 - Sair do programa\n'))

    if opcao == 1:      
        chave_n = 0
        chave_e = 0

        while chave_n != n and chave_e != e:
            chave_n = int(input('Informe a chave N: '))
            chave_e = int(input('Informe a chave E: '))

            if chave_n != n and chave_e != e:
                print('\nDados inválidos! Por favor insira as chaves geradas neste programa.\n')
                
        mensagem = input('Digite a mensagem a ser criptografada: ')

        mensagem_final = ''.join(chr(encripta(ord(i), e, n)) for i in mensagem)

        print(f'Texto criptografado: {mensagem_final}\n')

        descripto_mensagem()
    elif opcao == 2:
        print('\nObrigado por usar nosso programa!\n\nDesenvolvido por:\nAdriano Mello\nGustavo Lourenço\nLucas Rangel\nMatheus Oliveira\nNicolas Bianchi\n')
    else:
        print('\nValor inválido.\n\n')
        cripto_mensagem()

# Descriptografa a mensagem
def descripto_mensagem():

    opcao = int(input('Deseja descriptografar essa mensagem?\n1 - Descriptografar mensagem\n2 - Sair\n'))

    if opcao == 1:
        chave_n = 0
        chave_d = 0

        while chave_n != n and chave_d != d:
            chave_n = int(input('Informe a chave N: '))
            chave_d = int(input('Informe a chave D: '))

            if chave_n != n and chave_d != d:
                print('\nDados inválidos! Por favor insira as chaves geradas neste programa.\n')
        
        des_mensagem = ''.join(chr(descript(ord(i), d, n)) for i in mensagem_final)
        print(f'Texto descriptografado: {des_mensagem}\n')

        opcao = int(input('Informe os próximos passos:\n1 - Gerar novas chaves\n2 - Criptografar nova mensagem\n3 - Sair\n'))

        if opcao == 1:
            gerar_chaves()
        elif opcao == 2:
            cripto_mensagem()
        elif opcao == 3:
            print('\nObrigado por usar nosso programa!\n\nDesenvolvido por:\nAdriano Mello\nGustavo Lourenço\nLucas Rangel\nMatheus Oliveira\nNicolas Bianchi\n')
    elif opcao == 2:
        print('\nObrigado por usar nosso programa!\n\nDesenvolvido por:\nAdriano Mello\nGustavo Lourenço\nLucas Rangel\nMatheus Oliveira\nNicolas Bianchi\n')
    else:
        print('\nValor inválido.\n\n')
        descripto_mensagem()

menu()