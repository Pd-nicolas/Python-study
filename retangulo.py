
#algoritimo que calcula a area de um retangulo
def retangulo(b,h):
    calc = b * h
    return calc


base = float(input("Digite a largura do retangulo: "))
altura = float(input('Agora digite a altura do retangulo: '))

print('A área do retangulo é :' + str(retangulo(base,altura)))