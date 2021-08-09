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



def calculo(simbolo_matematico, dificuldade):
    """
    Vai mostrar o calculo conforme sua dificuldade
    e simbolo matematico.

    :param simbolo_matematico:
            Serve para escolher o simbolo matematico
            EX:
                1 -> Soma
                2 -> Subtracao
                3 -> Divisao
                4 -> Multiplicacao

    :param dificuldade:
            Serve para escolher a dificuldade
            EX:
                1 -> Facil (de 1 a 100)
                2 -> Normal (de 20 a 150)
                3 -> Dificil (de 100 a 500)
                4 -> Desafie-me (de 1000 a 3000)
    :return: None
    """
    if simbolo_matematico == 1:     # Se for soma
        if dificuldade == 1:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(1, 100)    # Dificuldade facil vai de 1 a 100
                n2 = randint(1, 100)
                try:
                    pular(2)
                    print('__' * 15)
                    resultado = int(input(f'{n1} + {n2} = '))
                except:
                    print('\n\n\033[1;31mDigite o resultado da soma\033[m')
                else:
                    if type(resultado) == int:
                        if resultado == n1 + n2:
                            print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                        elif resultado == 0:
                            break
                        else:
                            print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 + n2}\033[m.')
                    else:
                        print('\n\n\033[1;31mDigite o resultado da soma\033[m')
        elif dificuldade == 2:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(20, 150)  # Dificuldade normal vai de 20 a 150
                n2 = randint(20, 150)
                try:
                    pular(2)
                    print('__' * 15)
                    resultado = int(input(f'{n1} + {n2} = '))
                except:
                    print('\n\n\033[1;31mDigite o resultado da soma\033[m')
                else:
                    if type(resultado) == int:
                        if resultado == n1 + n2:
                            print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                        elif resultado == 0:
                            break
                        else:
                            print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 + n2}\033[m.')
                    else:
                        print('\n\n\033[1;31mDigite o resultado da soma\033[m')
        elif dificuldade == 3:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(100, 500)  # Dificuldade dificil vai de 100 a 500
                n2 = randint(100, 500)
                try:
                    pular(2)
                    print('__' * 15)
                    resultado = int(input(f'{n1} + {n2} = '))
                except:
                    print('\n\n\033[1;31mDigite o resultado da soma\033[m')
                else:
                    if type(resultado) == int:
                        if resultado == n1 + n2:
                            print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                        elif resultado == 0:
                            break
                        else:
                            print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 + n2}\033[m.')
                    else:
                        print('\n\n\033[1;31mDigite o resultado da soma\033[m')
        elif dificuldade == 4:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(1000, 3000)  # Dificuldade desafie-me vai de 1000 a 3000
                n2 = randint(1000, 3000)
                try:
                    pular(2)
                    print('__' * 15)
                    resultado = int(input(f'{n1} + {n2} = '))
                except:
                    print('\n\n\033[1;31mDigite o resultado da soma\033[m')
                else:
                    if type(resultado) == int:
                        if resultado == n1 + n2:
                            print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                        elif resultado == 0:
                            break
                        else:
                            print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 + n2}\033[m.')
                    else:
                        print('\n\n\033[1;31mDigite o resultado da soma\033[m')
    elif simbolo_matematico == 2:   # Se for subtracao
        if dificuldade == 1:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(1, 100)  # Dificuldade facil vai de 1 a 100
                n2 = randint(1, 100)
                if n1 > n2:
                    try:
                        pular(2)
                        print('__' * 15)
                        resultado = int(input(f'{n1} - {n2} = '))
                    except:
                        print('\n\n\033[1;31mDigite o resultado da subtracao\033[m')
                    else:
                        if type(resultado) == int:
                            if resultado == n1 - n2:
                                print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                            elif resultado == 0:
                                break
                            else:
                                print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 - n2}\033[m.')
                        else:
                            print('\n\n\033[1;31mDigite o resultado da subtracao\033[m')
        elif dificuldade == 2:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(20, 150)
                n2 = randint(20, 150)
                if n1 > n2:
                    try:
                        pular(2)
                        print('__' * 15)
                        resultado = int(input(f'{n1} - {n2} = '))
                    except:
                        print('\n\n\033[1;31mDigite o resultado da subtracao\033[m')
                    else:
                        if type(resultado) == int:
                            if resultado == n1 - n2:
                                print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                            elif resultado == 0:
                                break
                            else:
                                print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 - n2}\033[m.')
                        else:
                            print('\n\n\033[1;31mDigite o resultado da subtracao\033[m')
        elif dificuldade == 3:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(100, 500)
                n2 = randint(100, 500)
                if n1 > n2:
                    try:
                        pular(2)
                        print('__' * 15)
                        resultado = int(input(f'{n1} - {n2} = '))
                    except:
                        print('\n\n\033[1;31mDigite o resultado da subtracao\033[m')
                    else:
                        if type(resultado) == int:
                            if resultado == n1 - n2:
                                print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                            elif resultado == 0:
                                break
                            else:
                                print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 - n2}\033[m.')
                        else:
                            print('\n\n\033[1;31mDigite o resultado da subtracao\033[m')
        elif dificuldade == 4:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(1000, 3000)
                n2 = randint(1000, 3000)
                if n1 > n2:
                    try:
                        pular(2)
                        print('__' * 15)
                        resultado = int(input(f'{n1} - {n2} = '))
                    except:
                        print('\n\n\033[1;31mDigite o resultado da subtracao\033[m')
                    else:
                        if type(resultado) == int:
                            if resultado == n1 - n2:
                                print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                            elif resultado == 0:
                                break
                            else:
                                print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 - n2}\033[m.')
                        else:
                            print('\n\n\033[1;31mDigite o resultado da subtracao\033[m')
    elif simbolo_matematico == 3:   # Se for multiplicacao
        if dificuldade == 1:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(1, 100)
                n2 = randint(1, 100)
                try:
                    pular(2)
                    print('__' * 15)
                    resultado = int(input(f'{n1} x {n2} = '))
                except:
                    print('\n\n\033[1;31mDigite o resultado da multiplicacao\033[m')
                else:
                    if type(resultado) == int:
                        if resultado == n1 * n2:
                            print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                        elif resultado == 0:
                            break
                        else:
                            print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 * n2}\033[m.')
                    else:
                        print('\n\n\033[1;31mDigite o resultado da multiplicacao\033[m')
        elif dificuldade == 2:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(20, 150)
                n2 = randint(20, 150)
                try:
                    pular(2)
                    print('__' * 15)
                    resultado = int(input(f'{n1} x {n2} = '))
                except:
                    print('\n\n\033[1;31mDigite o resultado da multiplicacao\033[m')
                else:
                    if type(resultado) == int:
                        if resultado == n1 * n2:
                            print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                        elif resultado == 0:
                            break
                        else:
                            print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 * n2}\033[m.')
                    else:
                        print('\n\n\033[1;31mDigite o resultado da multiplicacao\033[m')
        elif dificuldade == 3:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(100, 500)
                n2 = randint(100, 500)
                try:
                    pular(2)
                    print('__' * 15)
                    resultado = int(input(f'{n1} x {n2} = '))
                except:
                    print('\n\n\033[1;31mDigite o resultado da multiplicacao\033[m')
                else:
                    if type(resultado) == int:
                        if resultado == n1 * n2:
                            print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                        elif resultado == 0:
                            break
                        else:
                            print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 * n2}\033[m.')
                    else:
                        print('\n\n\033[1;31mDigite o resultado da multiplicacao\033[m')
        elif dificuldade == 4:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(1000, 3000)
                n2 = randint(1000, 3000)
                try:
                    pular(2)
                    print('__' * 15)
                    resultado = int(input(f'{n1} x {n2} = '))
                except:
                    print('\n\n\033[1;31mDigite o resultado da multiplicacao\033[m')
                else:
                    if type(resultado) == int:
                        if resultado == n1 * n2:
                            print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                        elif resultado == 0:
                            break
                        else:
                            print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 * n2}\033[m.')
                    else:
                        print('\n\n\033[1;31mDigite o resultado da multiplicacao\033[m')
    elif simbolo_matematico == 4:   # Se for divisao
        if dificuldade == 1:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(2, 100)
                n2 = randint(2, 100)
                if n1 % n2 == 0 and n1 > n2:
                    try:
                        pular(2)
                        print('__' * 15)
                        resultado = int(input(f'{n1} / {n2} = '))
                    except:
                        print('\n\n\033[1;31mDigite o resultado da divisao\033[m')
                    else:
                        if type(resultado) == int:
                            if resultado == n1 / n2:
                                print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                            elif resultado == 0:
                                break
                            else:
                                print(f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 / n2}\033[m.')
                        else:
                            print('\n\n\033[1;31mDigite o resultado da divisao\033[m')
        elif dificuldade == 2:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(20, 150)
                n2 = randint(2, 150)
                if n1 % n2 == 0 and n1 > n2:
                    try:
                        pular(2)
                        print('__' * 15)
                        resultado = int(input(f'{n1} / {n2} = '))
                    except:
                        print('\n\n\033[1;31mDigite o resultado da divisao\033[m')
                    else:
                        if type(resultado) == int:
                            if resultado == n1 / n2:
                                print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                            elif resultado == 0:
                                break
                            else:
                                print(
                                    f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 / n2}\033[m.')
                        else:
                            print('\n\n\033[1;31mDigite o resultado da divisao\033[m')
        elif dificuldade == 3:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(100, 500)
                n2 = randint(2, 500)
                if n1 % n2 == 0 and n1 > n2:
                    try:
                        pular(2)
                        print('__' * 15)
                        resultado = int(input(f'{n1} / {n2} = '))
                    except:
                        print('\n\n\033[1;31mDigite o resultado da divisao\033[m')
                    else:
                        if type(resultado) == int:
                            if resultado == n1 / n2:
                                print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                            elif resultado == 0:
                                break
                            else:
                                print(
                                    f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 / n2}\033[m.')
                        else:
                            print('\n\n\033[1;31mDigite o resultado da divisao\033[m')
        elif dificuldade == 4:
            pular(30)
            print(f'\033[;31m{"Resolva o calculo":^50}\033[m')
            print(f'{"Digite 0 para voltar":^50}')
            pular(5)
            while True:
                n1 = randint(1000, 3000)
                n2 = randint(2, 3000)
                if n1 % n2 == 0 and n1 > n2:
                    try:
                        pular(2)
                        print('__' * 15)
                        resultado = int(input(f'{n1} / {n2} = '))
                    except:
                        print('\n\n\033[1;31mDigite o resultado da divisao\033[m')
                    else:
                        if type(resultado) == int:
                            if resultado == n1 / n2:
                                print('\n\n\033[1;32mParabens\033[m!! Voce acertou.')
                            elif resultado == 0:
                                break
                            else:
                                print(
                                    f'\n\nVoce \033[1;31merrou\033[m...\nA resposta era \033[;1m{n1 / n2}\033[m.')
                        else:
                            print('\n\n\033[1;31mDigite o resultado da divisao\033[m')
