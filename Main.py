from Funcoes import *

while True:
    certeza = ''    # Variavel global para ter a certeza que o usuario deseja encerrar/fechar o jogo.
    titulo_inicial()
    press_enter()
    # Menu inicial
    while True:
        pular(30)
        print(f'\033[;1m{"Menu Principal":^50}\033[m')
        pular(2)
        try:
            escolha = int(input("""Digite o numero de uma das opcões abaixo;


1 \033[1;31m➤\033[m Iniciar

2 \033[1;31m➤\033[m Informacões

3 \033[1;31m➤\033[m Sair



Escolha: """))
        except:
            erro(msg='Digite um dos valores\ninformados na tela.')
            pular(30)
        else:
            if escolha == 1:    # Escolheu iniciar o jogo (Pendente).
                while True:
                    pular(30)
                    print(f'\033[31;1m{"Modos":^50}\033[m')
                    pular(2)
                    try:
                        modo = int(input("""Digite o numero de uma das opções abaixo;
                    
                    
1 \033[1;31m➤\033[m Soma

2 \033[1;31m➤\033[m Subtracao

3 \033[1;31m➤\033[m Multiplicacao

4 \033[1;31m➤\033[m Divisao


5 \033[1;31m➤\033[m \033[;1mVoltar\033[m



Escolha: """))
                    except:
                        erro(msg='Digite um dos valores\ninformados na tela.')
                        pular(30)
                    else:
                        if modo == 1:    # (pendente)
                            while True:
                                pular(30)
                                print(f'\033[1;31m{"Dificuldades":^50}\033[m')
                                pular(2)
                                try:
                                    dificuldade = int(input("""Digite o numero de uma das opcoes abaixo;
                                    
                                    
1 \033[1;31m➤\033[m Facil

2 \033[1;31m➤\033[m Normal (recomendado)

3 \033[1;31m➤\033[m Dificil

4 \033[1;31m➤\033[m Desafie-me


5 \033[1;31m➤\033[m \033[;1mVoltar\033[m



Escolha: """))
                                except:
                                    erro(msg='Digite um dos valores\ninformados na tela.')
                                    pular(30)
                                else:
                                    if dificuldade == 1:
                                        calculo(1, 1)
                                    elif dificuldade == 2:
                                        calculo(1, 2)
                                    elif dificuldade == 3:
                                        calculo(1, 3)
                                    elif dificuldade == 4:
                                        calculo(1, 4)
                                    elif dificuldade == 5:
                                        break
                                    else:
                                        erro(msg='Digite um dos valores\ninformados na tela.')
                                        pular(30)
                        elif modo == 2:  # (pendente)
                            while True:
                                pular(30)
                                print(f'\033[1;31m{"Dificuldades":^50}\033[m')
                                pular(2)
                                try:
                                    dificuldade = int(input("""Digite o numero de uma das opcoes abaixo;


1 \033[1;31m➤\033[m Facil

2 \033[1;31m➤\033[m Normal (recomendado)

3 \033[1;31m➤\033[m Dificil

4 \033[1;31m➤\033[m Desafie-me


5 \033[1;31m➤\033[m \033[;1mVoltar\033[m



Escolha: """))
                                except:
                                    erro(msg='Digite um dos valores\ninformados na tela.')
                                    pular(30)
                                else:
                                    if dificuldade == 1:
                                        calculo(2, 1)
                                    elif dificuldade == 2:
                                        calculo(2, 2)
                                    elif dificuldade == 3:
                                        calculo(2, 3)
                                    elif dificuldade == 4:
                                        calculo(2, 4)
                                    elif dificuldade == 5:
                                        break
                                    else:
                                        erro(msg='Digite um dos valores\ninformados na tela.')
                                        pular(30)
                        elif modo == 3:  # (pendente)
                            while True:
                                pular(30)
                                print(f'\033[1;31m{"Dificuldades":^50}\033[m')
                                pular(2)
                                try:
                                    dificuldade = int(input("""Digite o numero de uma das opcoes abaixo;


1 \033[1;31m➤\033[m Facil

2 \033[1;31m➤\033[m Normal (recomendado)

3 \033[1;31m➤\033[m Dificil

4 \033[1;31m➤\033[m Desafie-me


5 \033[1;31m➤\033[m \033[;1mVoltar\033[m



Escolha: """))
                                except:
                                    erro(msg='Digite um dos valores\ninformados na tela.')
                                    pular(30)
                                else:
                                    if dificuldade == 1:
                                        calculo(3, 1)
                                    elif dificuldade == 2:
                                        calculo(3, 2)
                                    elif dificuldade == 3:
                                        calculo(3, 3)
                                    elif dificuldade == 4:
                                        calculo(3, 4)
                                    elif dificuldade == 5:
                                        break
                                    else:
                                        erro(msg='Digite um dos valores\ninformados na tela.')
                                        pular(30)
                        elif modo == 4:  # (pendente)
                            while True:
                                pular(30)
                                print(f'\033[1;31m{"Dificuldades":^50}\033[m')
                                pular(2)
                                try:
                                    dificuldade = int(input("""Digite o numero de uma das opcoes abaixo;


1 \033[1;31m➤\033[m Facil

2 \033[1;31m➤\033[m Normal (recomendado)

3 \033[1;31m➤\033[m Dificil

4 \033[1;31m➤\033[m Desafie-me


5 \033[1;31m➤\033[m \033[;1mVoltar\033[m



Escolha: """))
                                except:
                                    erro(msg='Digite um dos valores\ninformados na tela.')
                                    pular(30)
                                else:
                                    if dificuldade == 1:
                                        calculo(4, 1)
                                    elif dificuldade == 2:
                                        calculo(4, 2)
                                    elif dificuldade == 3:
                                        calculo(4, 3)
                                    elif dificuldade == 4:
                                        calculo(4, 4)
                                    elif dificuldade == 5:
                                        break
                                    else:
                                        erro(msg='Digite um dos valores\ninformados na tela.')
                                        pular(30)
                        elif modo == 5:
                            break
                        else:
                            erro(msg='Digite um dos valores\ninformados na tela.')
                            pular(30)
            elif escolha == 2:  # Escolheu mostrar as informacoes do jogo.
                pular(30)
                print(f'\033[;1m{"Informacões":^50}\033[m')
                pular(3)
                print("""\033[1;31m▰\033[m Calculator
    É um jogo educacional para treinar sua matematica basica.
            
\033[1;31m▰\033[m Modos
    Soma, Subtracão, Multiplicação e Divisão.
    
\033[1;31m▰\033[m Em breve novas atualizacões.""")
                press_enter(c=1, msg='voltar')
                pular(30)
            elif escolha == 3:  # Escolheu encerrar o jogo.
                pular(30)
                while True:
                    try:
                        certeza = str(input('Tem certeza que deseja sair? [S/N] -> ')).upper().strip()[0]
                    except:
                        erro('Digite um dos valores\n\033[;1mS = sim | N = não\033[m')
                        pular(30)
                    else:
                        if certeza == 'S':
                            pular(30)
                            print('O programa foi encerrado com \033[;1msucesso\033[m.\n\n\033[;1mAte logo\033[m \033[1;31m❤\033[m')
                            break
                        elif certeza == 'N':
                            break
                        else:
                            erro('Digite um dos valores\n\033[;1mS = sim | N = não\033[m')
                            pular(30)
            else:
                erro(msg='Digite um dos valores\ninformados na tela.')
                pular(30)
            if certeza == 'S':
                break
    if certeza == 'S':
        break
