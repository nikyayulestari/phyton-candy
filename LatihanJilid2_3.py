print 'Mencari Nilai Terkecil dan Nilai Terbesar'
a=input('Masukkan Variabel 1 : ')
b=input('Masukkan Variabel 2 : ')
c=input('Masukkan Variabel 3 : ')
if a < b and a < c:
    print 'Nilai Terkecil adalah', a
elif b < a and b < c:
        print 'Nilai Terkecil adalah', b
elif c < a and c < b:
        print 'Nilai Terkecil adalah', c
if a > b and a > c:
    print 'Nilai Terbesar adalah', a
elif b > a and b > c:
        print 'Nilai Terbesar adalah', b
elif c > a and c > b:
        print 'Nilai Terbesar adalah', c
