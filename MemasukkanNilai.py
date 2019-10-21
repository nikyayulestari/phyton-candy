Indo = input('Masukkan Nilai Bahasa Indonesia : ')
Inggris = input('Masukkan Nilai Bahasa Inggris : ')
Matematika = input('Masukkan Nilai Matematika : ')
Produktif = input('Masukkan Nilai Produktif : ')
jumlah = Indo + Inggris + Matematika + Produktif
rata = jumlah/4
if rata >= 60:
    ket = 'Lulus'
else:
    ket = 'Tidak Lulus'
if rata >= 90:
    predikat = 'A'
elif rata >= 80:
     predikat = 'B'
elif rata >= 70:
     predikat = 'C'
else:
     predikat = 'D'
print 'Jumlah Nilai = ', jumlah
print 'Rata-rata Nilai = ', rata
print 'Keterangan = ', ket
print 'Predikat = ', predikat

