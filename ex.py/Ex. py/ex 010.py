real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.65
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))
