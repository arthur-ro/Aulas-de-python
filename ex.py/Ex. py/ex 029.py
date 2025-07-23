velocidade = float(input('Qual é a velocidade atual do seu carro?'))
if velocidade >80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você de pagar um multa de R${:.2f}'.format(multa))
print('tenha um bom dia! Dirija com segurança!')



