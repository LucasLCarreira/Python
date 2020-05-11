
def chamada(txt):
    print('-' * 40)
    print(f'{txt}'.center(40))
    print('-' * 40)


def novo(txt):
    arquivo = open(txt, 'a+')

def programa():
    while True:
        chamada('SISTEMA DE CADASTRO')
        try:
            opcao = int(input('[1] Cadastrar uma pessoa\n'
                              '[2] Mostrar a lista\n'
                              '[3] Finalizar programa\n'
                              'Digite sua opção: '))
            print('-' * 40)
            if opcao == 1:
                nome = str(input('Digite o nome: '))
                idade = str(input('Digite a idade: '))
                cadastro = open('../cadastro.txt', 'a')
                cadastro.write('\n' + nome)
                cadastro.write('\n' + idade)
                cadastro.close()
            elif opcao == 2:
                cadastro = open('../cadastro.txt', 'r')
                c = 0
                print(f'{"NOME":25}{"IDADE"}')
                for linha in cadastro:
                    if c % 2 != 0:
                        linha = linha.rstrip()
                        print(f'{linha:25}', end='')
                    else:
                        linha = linha.rstrip()
                        print(f'{linha}')
                    c += 1
                cadastro.close()
            elif opcao == 3:
                print('FIM!')
                break
            else:
                print('Digite uma opção válida!')
        except FileNotFoundError:
            print('Arquivo criado com sucesso!')
            novo('cadastro.txt')

programa()