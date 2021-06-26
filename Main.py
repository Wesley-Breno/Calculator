from Funcoes import *

while True:
    titulo_inicial()
    press_enter()
    # Menu inicial
    while True:
        pular(10)
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
            pular(17)
        else:
            if escolha == 1:
                print('iniciou')
            elif escolha == 2:
                pular(11)
                print(f'\033[;1m{"Informacões":^50}\033[m')
                pular(3)
                print("""\033[1;31m▰\033[m Calculator
    É um jogo educacional para treinar sua matematica basica.
            
\033[1;31m▰\033[m Modos
    Soma, Subtracão e Divisão.
    
\033[1;31m▰\033[m Em breve novas atualizacões.""")
                press_enter(c=1, msg='voltar')
                pular(17)
            elif escolha == 3:
                print('Saiu')
            else:
                erro(msg='Digite um dos valores\ninformados na tela.')
                pular(17)
