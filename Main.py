from Funcoes import *

while True:
    titulo_inicial()
    press_enter()
    # Menu inicial
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
    else:
        if escolha == 1:
            print('iniciou')
        elif escolha == 2:
            print('Informacões')
        elif escolha == 3:
            print('Saiu')
        else:
            erro(msg='Digite um dos valores\ninformados na tela.')
