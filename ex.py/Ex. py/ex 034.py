salário = float(input('Qual é o salário do seu funcionário? '))
if salário <=1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhva R${:.2f} passa a ganhar {:.2f} agora.'.format(salário, novo))


