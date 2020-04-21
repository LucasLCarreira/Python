# Exercício Python 076
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência
# Mostre uma listagem de preços, organizando os dados de forma tabular.

tupla = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,
            'Compasso',9.99,'Mochila',120.90,'Canetas',22.30,'Livro',34.90)
print('-'*40)
print(f'\033[1m{"LISTAGEM DE PREÇO":^40}\033[m')
print('-'*40)
for p in range(0,len(tupla),2):
    print(f'{tupla[p]:.<30}R$ {tupla[p+1]:>6.2f}')

