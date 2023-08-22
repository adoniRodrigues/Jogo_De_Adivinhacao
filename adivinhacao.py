print('******************************')
print('*****Jogo Da adivinhação******')
print('******************************')

numero_secreto = 7
chute = input('Digite seu numero: ')
chute = int(chute)
print('Voce digitou:', chute)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto
 
if(numero_secreto == chute):
    print('Voce acertou')
elif(maior):
    print('Você	errou!	O	seu	chute	foi	maior	que	o	número	secreto')
elif(menor):
    print('Você	errou!	O	seu	chute	foi	menor	que	o	número	secreto')


print('Fim do Jogo!!!')