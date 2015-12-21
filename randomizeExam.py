import ExaminationKata
import sys

picker = ExaminationKata.KataPicker()
# default rank value
rank = '9kyu'

if (len(sys.argv)>1):
    rank = sys.argv[1]

kata = picker.getExamKata(rank)
print('Your examination kata: '.upper() + ' + '.join(kata['normal']))
print('Your examination kata with variations: '.upper() + ' + '.join(kata['varia']))
print('Mandatory kata from previous ranks: '.upper() + ' + '.join(kata['previous']))
print('Extra kata: '.upper() + ' +'.join(kata['extras']))
print('Extra kata with variations: '.upper() + ' +'.join(kata['extrasVaria']))

