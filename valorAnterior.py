#exercicio: Escreva um algoritimo para ler um valor do teclado e mostrar o antecessor


#number = int(input("digite um numero: "))
#result = number - 1

#print('o antecessor ao ' + str(number) + " é: " + str(result)) #para concatenar precisa transformar os numeros em string




#usando função

def previousNumber(number):
    calc = (number - 1)
    return calc


number = int(input('Digite um numero e saberás qual é o antecessor: '))    #precisei transformar em int pra funcionar



print('O antecessor ao ' + str(number) + 'é: ' + str(previousNumber(number))) #precisei usar o str pra transformar em string novamente