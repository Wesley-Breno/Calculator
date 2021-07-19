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
                print('iniciou')
            elif escolha == 2:  # Escolheu mostrar as informacoes do jogo.
                pular(30)
                print(f'\033[;1m{"Informacões":^50}\033[m')
                pular(3)
                print("""\033[1;31m▰\033[m Calculator
    É um jogo educacional para treinar sua matematica basica.
            
\033[1;31m▰\033[m Modos
    Soma, Subtracão e Divisão.
    
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
