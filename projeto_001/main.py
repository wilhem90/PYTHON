print('\n-----------------------------------------------------------------------')
print("Swiv etap sa yo byen. \nMen lis eskzèsis yo: ")
print('\n--------------------------------------------------')
print('1 -KALKILATRIS BAZIK AVÈK 4 FONKSYON (+ - * /)')
print('2- KALKILE LAJ KENPÒT MOUN')
print('3- KONVÈTI TANPERATI F°/C°')
print('3- KALKILE MEDYA')
print('--------------------------------------------------\n')
listExo = ['1 -KALKILATRIS BAZIK AVÈK 4 FONKSYON (+ - * /)', '2- KALKILE LAJ KENPÒT MOUN', '3- KONVÈTI TANPERATI F°/C°', '4- KALKILE MEDYA']

#-----------------------------------------------------------------------------------------------------------------------
def KALKILATRIS():
    print('----------\nEkzèsis n° 001\n----------')
    val1 = input('Valè 1: ')
    val2 = input('Valè 2: ')
    if(val1.isnumeric() and val2.isnumeric()):
        while True:
            print('---------------')
            print('1- Adisyon')
            print('2- Soustraksyon')
            print('3- Divizyon')
            print('4- Miltiplikasyon')
            print('0- Meni prensipal')
            print('---------------')
            listOperasyon = ['1- Adisyon', '2- Soubstraksyon', '3- Divizyon', '4- Miltiplikasyon']
            operasyon = input('Ki operasyon ou vle fè: ')
            if(operasyon.isnumeric()):
                indexOper = int(operasyon) - 1
                if(int(operasyon) > 0 and int(operasyon) <= len(listOperasyon)):
                    if(indexOper == 0):
                        print('\n\nA soma entre ', val1, 'e', val2, ' = ', float(val1) + float(val2))
                    elif(indexOper == 1):
                        print('\n\nSoustraksyon entre ', val1, 'e', val2, ' = ', float(val1) - float(val2))
                    elif(indexOper == 2):
                        print('\n\nDiviksyon entre ', val1, 'e', val2, ' = ', float(val1) / float(val2))
                    elif(indexOper == 3):
                        print('\n\nMilitiplikasyon entre ', val1, 'e', val2, ' = ', float(val1) * float(val2))
                else:
                    print('---------------------------------')
                    if(int(indexOper) == -1):
                        break
                    else:
                        print('Ekzèsis sa poko disponib!')
            else:
                print('Ou dwe enfòme yon valè nimerik')
    else:
        print('Enfòme yon valè nimerik pou ou finalize operasyon an!')


def KALKILELAJ():
    print('----------\nEkzèsis n° 002\n----------')
    aneNesans = input('Ane nesans lan: ')
    if(aneNesans.isnumeric()):
        while True:
            print('---------------')
            print('Ane aktyèl: 2023')
            print('---------------')
            aneAktyèl = 2023
            if(aneNesans.isnumeric()):
                dateNesans = int(aneNesans)
                if(dateNesans >= 1900 and dateNesans <= aneAktyèl):
                    print('Ou fèt', dateNesans, 'Laj la se:',aneAktyèl - dateNesans, 'ane')
                    break
                else:
                    print('---------------------------------')
                    break
            else:
                print('Ou dwe enfòme yon valè nimerik')
    else:
        print('Enfòme yon valè nimerik pou ou finalize operasyon an!')


def TANPERATI():
    while True:
        print('----------\nEkzèsis n° 003\n----------')
        tanperati = input('Enfòme tanperati a °F: ')
        if(tanperati.isnumeric()):
            tanperati = float(tanperati)
            print('Tanperati aktyèl la:', tanperati, '°F')
            tanperati = int(tanperati)
            celcius = ((tanperati-32)*5)/9
            print('Tanperati a',celcius,'°C')
            break
        else:
            print('Ou dwe enfòme yon valè nimerik')

def MEDYA():
    alumnns = ['Wilhem Wundt Maxime', 'Gael Charles', 'Bernanrd Pelegrine', 'Hendy Bernard', 'Rita Pierre', 'Rosmanie Joseph', 'Lislor Hyppolite', 'Rubens Maxime', 'Herode Etienne', 'Milgot Pelegrine', 'Sunshine Pierre', 'Leveksy Paul']
    print('----------\nEkzèsis n° 004\n----------')
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
    
#-----------------------------------------------------------------------------------------------------------------------

while True:
    print('\n                          Meni Prensipal')
    print('-----------------------------------------------------------------------')
    print("Swiv etap sa yo byen. \nMen lis eskzèsis yo: ")
    print('--------------------------------------------------')
    print('1 -KALKILATRIS BAZIK AVÈK 4 FONKSYON (+ - * /)')
    print('2- KALKILE LAJ KENPÒT MOUN')
    print('3- KONVÈTI TANPERATI F°/C°')
    print('4- KALKILE MEDYA')
    print('0- SI OU VLE FEMEN PWOGRAM NAN')
    print('--------------------------------------------------\n')

    exo = input('Ki ekzèsis ou vle fè: ')
    if(exo.isnumeric()):
        indexExo = int(exo) - 1
        if(int(exo) > 0 and int(exo) <= len(listExo)):
            if(indexExo == 0):
                KALKILATRIS()
            elif(indexExo == 1):
                KALKILELAJ()
            elif(indexExo == 2):
                TANPERATI()
            elif(indexExo == 3):
                MEDYA()
        else:
            if(indexExo <= 0):
                print('\nPwogram nan femen!\n')
                break
            else:
                print('Nimewo ekzèsis sa a poko disponib!')
    else:
        print('Enfòme yon valè nimerik!')