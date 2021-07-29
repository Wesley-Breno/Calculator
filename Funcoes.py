from random import randint


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


def calculo(dif):
    if dif == 1:
        while True:
            pular(30)
            print(f'\033[31;1m{"Escolha um dos modos":^50}\033[m')
            pular(3)
            try:
                modo = int(input("""1 \033[1;31m➤\033[m Soma

2 \033[1;31m➤\033[m Subtração

3 \033[1;31m➤\033[m Multiplicação


4 \033[1;31m➤\033[m \033[;1mVoltar\033[m



Escolha: """))
            except:
                erro(msg='Digite um dos valores\ninformados na tela.')
                pular(30)
            else:
                if modo == 1:
                    pular(30)
                    print(f'\033[;31m{"_- Resolva o calculo abaixo -_":^50}\033[m')
                    print(f'{"Digite 0 para voltar":^50}')
                    pular(3)
                    while True:
                        n1 = randint(10, 100)
                        n2 = randint(10, 100)
                        try:
                            print('__' * 7)
                            resultado = int(input(f'{n1} + {n2} = '))
                        except:
                            erro('Digite o resultado do calculo.')
                            pular(10)
                        else:
                            if resultado == n1 + n2:
                                print('Voce \033[1;32macertou\033[m!\n')
                            elif resultado == 0:
                                break
                            else:
                                print(f'Voce \033[1;31merrou\033[m!\nReposta certa: \033[;1m{n1 + n2}\033[m\n')
                else:
                    erro(msg='Digite um dos valores\ninformados na tela.')
                    pular(30)
    elif dif == 2:  # (pendente)
        pass
    elif dif == 3:  # (pendente)
        pass
    else:
        erro(msg='Houve um erro\nPor favor tente novamente.')

