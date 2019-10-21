print 'Menu Pilihan :'
print '1. Konversi Reamur'
print '2. Konversi Romer'
print '3. Keluar'
pilihan = input ('Masukkan Pilihan : ')
if pilihan == 1 :
    angka = input('Masukkan Angka Reamur : ')
    kelvin = angka/0.8+273.15
    celcius = angka/0.8
    fahrenheit = angka*2.25+32
    rankine = angka*2.25+491.67
    delisle = (80-angka)*1.875
    newton = angka*33/80
    romer = angka*21/32+7.5
    print 'Kelvin = ', kelvin
    print 'Celcius = ', celcius
    print 'Fahrenheit = ', fahrenheit
    print 'Rankine = ', rankine
    print 'Delisle = ', delisle
    print 'Newton = ', newton
    print 'Romer = ', romer
elif pilihan == 2 :
    angka = input('Masukkan Angka Reamur : ')
    kelvin = (angka-7.5)*40/21+273.15
    celcius = (angka-7.5)*40/21
    fahrenheit = (angka-7.5)*24/7+32
    rankine = (angka-7.5)*24/7+491.67
    delisle = (60-angka)*20/7
    newton = (angka-7.5)*22/35
    romer = (angka-7.5)*32/21
    print 'Kelvin = ', kelvin
    print 'Celcius = ', celcius
    print 'Fahrenheit = ', fahrenheit
    print 'Rankine = ', rankine
    print 'Delisle = ', delisle
    print 'Newton = ', newton
    print 'Romer = ', romer
else :
    exit
