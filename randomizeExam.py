import ExaminationKataConf
import ExaminationKata
import sys

picker = ExaminationKata.KataPicker(ExaminationKataConf)
# default rank value
rank = '9kyu'
userInput = ''

if (len(sys.argv)>1):
    userInput = sys.argv[1]

if userInput == '--help':
    print('Choose from following ranks: %s' % ExaminationKataConf.ranks.join(','))
else: 
    if userInput not in ExaminationKataConf.ranks:
        print('\nUnknown rank - dafaulting to 9kyu')
        rank = '9kyu'
    else:
        rank = userInput

    kata = picker.getExamKata(rank)
    print('\nYour examination kata: '.upper() + ' + '.join(kata['normal']))
    print('Your examination kata with variations: '.upper() + ' + '.join(kata['varia']))

    if len(kata['previous']) > 0:
        print('\nMandatory kata from previous ranks: '.upper() + ' + '.join(kata['previous']))

    print('\nExtra kata: '.upper() + ' +'.join(kata['extras']))
    print('Extra kata with variations: '.upper() + ' +'.join(kata['extrasVaria']))