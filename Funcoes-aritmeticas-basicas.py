#demonstração de uso de funções aritméticas básicas no Python
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('Soma: {soma}. \nSubtração: {sub}. \nMultiplicação: {mult}. \nDivisão: {div}. \nResto: {rest}'
      .format(soma=soma, sub=subtracao, mult=multiplicacao, div=divisao, rest=resto))