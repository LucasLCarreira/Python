# Exercício Python 083
# Crie um progreama onde o usuário digite uma expressão matemática qualquer que use parênteses
# Seu aplicativo deverá analisar se a expressão está com os parenteses na ordem correta.

expressao = str(input('Digite uma expressão matemática: ')).strip()
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')

expr = str(input("Digite uma expressão:"))
contagem = 0
for simbolo in expr:
    if simbolo == "(":
        contagem += 1
    if simbolo == ")":
        contagem -= 1
    if contagem < 0:
        break
if contagem == 0:
    print("Sua expressão é valida!!!")
else:
    print("Sua expressão é invalida!!!")