print 'Struktur if bersarang'
status = raw_input('Masukkan status (P=Pelanggan, N=Non Pelanggan) : ')
JLF = input('Masukkan jumlah lembar fotokopi : ')
if status == 'P':
    HPP = 75.0
elif status == 'N':
    if JLF < 100:
        HPP = 100.0
    else:
        HPP = 85.0
TH = JLF * HPP
print 'Total harga fotokopi = Rp.', TH
