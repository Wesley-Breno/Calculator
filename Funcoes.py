def titulo_inicial():
    """
    Ira escrever o titulo do jogo... "Calculator".

    :return: None
    """
    print()
    print('\033[;1m⟶-⟷-⟵' * 10)
    print(f'{"Calculator":^50}')
    print('⟶-⟷-⟵' * 10)
    print('\033[m')


def pular(c=1):
    """
    Serve para pular linhas.

    :param c:
            Escolha quantas linhas a funcão vai pular.

    :return: None
    """
    cont = 0
    while cont != c:
        print()
        cont += 1


def press_enter(c=0, msg='continuar'):
    """
    Aparece uma mensagem para o usuario apertar Enter
    para continuar a execuçao do programa.

    :param c:
            Serve para escolher a cor que a palavra Enter estara...
            c = 0
                Deixa em negrito
            c = 1
                Deixa em vermelho+negrito
            c = 2
                Deixa em roxo+negrito
            c = 3
                Deixa em azul+negrito

    :param msg:
            Serve para deixar o 'continuar' ou outra palavra.
            Ex:
                Digite Enter para continuar/sair.

    :return: None
    """
    if c == 0:
        # Negrito
        print()
        print('__' * 16)
        input(f'Pressione \033[;1mEnter\033[m para {msg}.')
    elif c == 1:
        # Vermelho
        print()
        print('__' * 16)
        input(f'Pressione \033[1;31mEnter\033[m para {msg}.')
    elif c == 2:
        # Roxo
        print()
        print('__' * 16)
        input(f'Pressione \033[35;1mEnter\033[m para {msg}.')
    elif c == 3:
        # Azul
        print()
        print('__' * 16)
        input(f'Pressione \033[34;1mEnter\033[m para {msg}.')


def erro(msg='padrao'):
    """
    Vai aparecer uma mensagem de erro na tela.

    :param msg:
            Mensagem personalizada... para caso seja um
            erro em especifico.

    :return: None
    """
    if msg != 'padrao':
        pular(3)
        print('__' * 16)
        print(f'[\033[1;31mERROR\033[m]\n{msg}')
        press_enter(c=1)
    else:
        pular(3)
        print('__' * 16)
        print('[\033[1;31mERROR\033[m]\nParece que houve um erro\nTente novamente.')
        press_enter(c=1)
