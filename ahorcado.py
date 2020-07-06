print('juguemos al\n AHORCADO')


palabraAdivinar = ''
listaPalabraAdivinar = []
listaPalabraMostrar = []
intentos = 5
letra = ''
run = True

palabraAdivinar = input('Dime una palabra: ')
listaPalabraAdivinar = list(palabraAdivinar)

# espacios \n para que no veas la palabra

print('\n\n\n\n\n\n\n\n\n')

for item in listaPalabraAdivinar:
    listaPalabraMostrar.append('_')

'''explication del range: comienza en 0, lo *2, luego le sumo 2 hasta que sea menor a 10, si se pasa, se va al for
n = 0
while n < 10:
    print(n*2)
    n += 2
for n in range(10):
    print(n * 2)'''

while run:
    ''' el join te une una lista, input una oración'''

    print(' '.join(listaPalabraMostrar))
    letra_adivinada = input('Dame una letra: ')

    # len devuelve el tamaño de la lista
    if len(letra_adivinada) != 1:
        print(' eh wachin, pone una sola letra')
        #continue saltea hasta la siguiente iteracion
        continue

    fallo = True
    n = 0
    for letra in listaPalabraAdivinar:
        if letra == letra_adivinada:
            fallo = False
            listaPalabraMostrar[n] = letra
        n += 1

    if fallo:
        intentos = intentos - 1
        print('Has fallado, te quedan ' + str(intentos) + ' intentos')

        if intentos == 0:
            print('Has perdido baboso')
            print('la palabra era ' + ''.join(listaPalabraAdivinar))
            run = False

    else:
        print('Has acertado')

        if '_' not in listaPalabraMostrar:
            print('HAS GANADO')
            print('la palabra era ' + ''.join(listaPalabraAdivinar))










