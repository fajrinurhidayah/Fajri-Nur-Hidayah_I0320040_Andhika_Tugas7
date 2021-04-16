#Program dengan 3 fungsi numerik
header =('PROGRAM DENGAN 3 FUNGSI NUMERIK')
print(header.center(80,'='))

list_angka = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#max & min
import math
print('\nAngka yang tersedia: ', list_angka)
print('Nilai minimum = ', min(list_angka), 'dan nilai maximum = ', max(list_angka))

#Random
import random
hasil_random = random.choice(list_angka)
print('\nAngka random yang diambil dari angka yang tersedia: ', hasil_random )

#sqrt
print('Akar dari', hasil_random, 'adalah', math.sqrt(hasil_random))

