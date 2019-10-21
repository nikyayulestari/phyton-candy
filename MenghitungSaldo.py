print 'PT. BANK ABC'
print '============================================================='
saldo = input('Saldo : Rp. ')
print 'Menu Transaksi'
print '1. Setor Tabungan'
print '2. Ambil Tabungan'
print '3. Exit'
menu = input('Pilihan Menu (1/2/3) ? ')
if menu == 1:
    setor = input('Masukkan Jumlah Rupiah yang akan disetor = Rp. ')
    jumlah = saldo + setor
    print 'Jumlah saldo = Rp. ', jumlah
elif menu == 2:
    tarik = input('Masukkan Jumlah Rupiah yang akan ditarik = Rp. ')
    jumlah = saldo - tarik
    if jumlah<10000:
        print '***********************************************************************************************'
        print 'Penarikan ditolak !'
        print 'Bank membuat kebijakan bahwa saldo minimum yang harus disisakan di rekening adalah Rp. 10.000,-'
        print '***********************************************************************************************'
        print 'Jumlah saldo Anda = ', saldo
    else:
        print 'Jumlah saldo = Rp. ', jumlah
else:
    exit
