print 'Nilai Ujian Mata Pelajaran Pemrograman Web'
NIM = raw_input('Nomor Induk Siswa : ')
nama = raw_input('Nama Siswa : ')
NUTS = input('Nilai Ujian Tengah Semester : ')
if NUTS > 70:
    NA = NUTS
    status = 'Lulus'
else:
    NUAS = input('Nilai Ujian Akhir Semester : ')
    NA = (NUTS * 0.4) + (NUAS * 0.6)
    if NA >= 60:
        status = 'Lulus'
    else:
        status = 'Tidak Lulus'

# format output
print ''
print ''
print 'Hasil Akhir :'
print '%-8s%-20s%-5s%-12s' % ('NIM', 'Nama', 'NA', 'Status')

length = len('%-8s%-20s%-5s%-15s' % ('NIM', 'Nama', 'NA', 'Status'))
print '=' * length
print '%-8s%-20s%-5s%-12s' % (NIM, nama, NA, status)
