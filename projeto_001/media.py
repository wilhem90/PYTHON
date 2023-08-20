alumnns = ['Wilhem Wundt Maxime', 'Gael Charles', 'Bernanrd Pelegrine', 'Hendy Bernard', 'Rita Pierre', 'Rosmanie Joseph', 'Lislor Hyppolite', 'Rubens Maxime', 'Herode Etienne', 'Milgot Pelegrine', 'Sunshine Pierre', 'Leveksy Paul']
qtnota = int(input('Digite qt notas: '))
for i in alumnns:
    print('\n----------------------------',i,'----------------------------')
    soma = 0
    media = 0
    indexNota = 1
    recebeqt = qtnota
    while recebeqt:
        notaEntrada = input(f'Digite nota {indexNota}: ')
        if(notaEntrada.isnumeric()):
            if(int(notaEntrada) <= 10):
                indexNota += 1
                soma += int(notaEntrada)
                recebeqt -= 1
                media = soma/(indexNota-1)
            else:
                print('----- Essa nota não esta correta! -----')
        else:
            print('----- Error: Ouffffff Deve informar um valor numerico! -----')
    print('Alumno(a): ',i)
    print('Notas toal: ', soma)
    print('A media dele(a) é: ',media,' pts.')
    if(media >= 7):
        print('Alumno(a) foi aprovado(a)')
    else:
        print('Alumno(a) foi reprovado(a)!')