# Biblioteca de cores:
amarelo = '\33[93m'
azul = '\33[94m'
verde = '\33[92m'
lilas = '\33[95m'
vermelho = '\33[91m'

# Estrutura de dados - Listas
candidatos = []
aprovados = []

#Função de título do programa
def titulo(msg):
    print('\n')
    print(f'{verde}='*62)
    print(f'{msg:^{62}}')
    print(f'='*62)
titulo('PROGRAMA DE VERIFICAÇÃO DE COMPATIBILIDADE PARA UMA VAGA')

# Função é das acões a serem tomadas pelo usuário do programa
def inicio():
    print(f'\n{azul}[1] Cadastrar candidato'
          f'\n[2] Informação sobre o Programa'
          f'\n[3] Sair')
    escolha = input(f'{lilas}Por gentileza escolher uma opção: ')
    if escolha == str(1):
        cadastrar()
    elif escolha == str(2):
        programador ()
    elif escolha == str(3):
        sair()
    else:
        print(f'{vermelho}\nALERTA - Ocorreu um erro na digitação!')
        inicio()

# Função de cadastrar os dados do candidato em tupla e depois inserir a ela na lista de candidatos
def cadastrar():
    print(f'{amarelo}\nPor gentileza cadastrar o candidato:')
    nome = input(f'{verde}\nNome do candidato: ').title()
    entrevista = float(input('Nota da entrevista: '))
    teorico = float(input('Nota do teste teórico: '))
    pratico = float(input('Nota do teste prático: '))
    sofl = float(input('Nota da avaliação de soft skills: '))
    pontuacao = str(f'e{entrevista}_t{teorico}_p{pratico}_s{sofl}')
    dados = [nome, pontuacao]
    candidatos.append(dados)
    print('\n')
    print(f'{amarelo}-'*42+f'\n          CANDIDATO CADASTRADO\n'+'-'*42) # Mensagem informando que o cadastro foi finalizado

    print(f'{azul}') #  listas de ações a serem tomadas
    print('\n[1] Cadastrar um novo candidato(a)' 
          '\n[2] Verificação de compatibilidade'
          '\n[3] Sair  ')

    op = input(f'{lilas}Por gentileza escolher um opção: ') # Estrutura de condição para açóes do usuário.
    if op == str(1):
        cadastrar()
    elif op == str(2):
        verificacao()
    elif op == str(3):
        sair()
    else:
        print(f'{vermelho}\nALERTA - Ocorreu um erro na digitação!')
        opçãoErro()


# Inicio da função de verificação com o direcionamento  de notas de cortes
def verificacao():
    print(f'{amarelo}\nPeencher as notas de corte abaixo: \n')
    ecorte = float(input(f'{verde}Nota da entrevista: '))
    tcorte = float(input('Nota do teste teórico: '))
    pcorte = float(input('Nota do teste prático: '))
    scorte = float(input('Nota da avaliação de soft skills: '))

    # Dentro do loop for, o código extrai as notas de cada avaliação, procurando nos índices e,t,p,s
    # dentro da lista candidatos.
    for i in range(len(candidatos)):
        eindex = candidatos[i][1].index('e')
        tindex = candidatos[i][1].index('t')
        pindex = candidatos[i][1].index('p')
        sindex = candidatos[i][1].index('s')

        # Extraindo a string posterior ao indices e anterior ao string "_" e transformando essa string extraida
        # em um valor float para análise de condição
        ei = float(candidatos[i][1][eindex + 1:tindex - 1])
        ti = float(candidatos[i][1][tindex + 1:pindex - 1])
        pi = float(candidatos[i][1][pindex + 1:sindex - 1])
        si = float(candidatos[i][1][sindex + 1:])

        # Condicionamento com o if, em que os candidatos que tiverem as notas maiores que a notas de cortes
        # irão para lista de aprovados.
        if ei >= ecorte and ti >= tcorte and pi >= pcorte and si >= scorte:
            aprovados.append(candidatos[i][0])

    print(f'\n{amarelo}Candidatos aprovados:')
    # Condicionaal if para verificar se está a lista está vazia ou não
    if len(aprovados) > 0:
        for i in aprovados: # Dentro do loop for, imprimirar os candidatos aprovados
            print(f'{verde}{i}')
    else:
        print(f'{vermelho}\nNenhum candidado foi aprovado!')
    print(f'\n{amarelo}Fim de execução!')
    sair()

# Texto com a informação do programa
def programador():
    print(f'\n{verde}INFORMAÇÃO DO PROGRAMA:'
    f'\n'
    f'\n    O progrma foi desenvolvido pelo Luiz Xavier, estudante do Curso de Análise de Dados'
    f'\ncom Python, promovido pelas Instituições de Ensino Resília e Senac em parceiria.'
    f'\n'
    f'\n    Corresponde ao projeto individual do Módulo 02, orientado pela professora Simone e '
    f'\ntem como proposta a elaboração de um aplicativo  em que uma startup possa  verificar a  compatibilidade de '
    f'\num candidato para uma determinada vaga, de acordo com o seu resultado nas etapas do processo seletivo.'
    f'\n'
    f'\n{lilas}[1] Cadastrar candidato\n[2] Sair do programa\n')
    opcao = input(f'{azul}Por gentileza escolher uma das opções: ')
    if opcao == str(1):
        cadastrar()
    elif opcao == str(2):
        sair()
    else:
        print(f'{vermelho}\nALERTA - Ocorreu um erro na digitação!')
        opçãoErro()


def opçãoErro():
    print(f'{azul}')  # Opção para erros
    print('\n[1] Cadastrar um novo candidato(a)'
          '\n[2] Verificação de compatibilidade'
          '\n[3] Sair  ')
    op = input(f'{lilas}Por gentileza escolher um opção: ')  # Estrutura de condição para açóes do usuário.
    if op == str(1):
        cadastrar()
    elif op == str(2):
        verificacao()
    elif op == str(3):
        sair()
    else:
        print(f'{vermelho}\nALERTA - Ocorreu um erro na digitação!')
        opçãoErro()


# Função para encerrar o programa
def sair():
    return print(f'\n{vermelho}PROGRAMA ENCERRADO e OBRIGADO!')



inicio()
