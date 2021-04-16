#Program dengan 3 fungsi string
header = 'Program dengan 3 fungsi string'
print( '\njudul awal: ')
print(header)

#Upper
Upper = (header.upper())
print('\nJudul setelah diberi upper: ')
print(Upper)

#Center
Center = Upper.center(50,'=')
print('\n Judul yang diberi center: ')
print(Center)

#count
print('\nBanyaknya huruf R dalam judul: ', Upper.count('R'))


