#Nama : Freany Mellyn Usmany
#Nim : 71200644
#Prodi : Teknik Informatika
#Universitas Kristen Duta Wacana


'''Kiki adalah siswa kelas sebelas di Sma Negeri 1  Yogyakarta,dan ia juga sedang mengikuti kepengurusan
organisasi osis dan menjadi pengurus bendahara .Organisasi osis ini berencana melakukan sebuah kegiatan 
perlobaan tingkat sekolah untuk memperingati hari kemerdekaan indonesia.
karena kiki adalah bendahara ia bertugas mencatat semua hal terkait jumlah pengeluaran uang yang akan digunaakan 
untuk mendanai kegiatan perlombaan tersebut.
Disini jumlah dana yang tersedia untuk mendanai perlombaan ini sebesar Rp.3500.000.
dan kiki sudah mencatat pengeluaran apa saja yang akan dikeluarkan untuk kegiatan tersebut .
jenis pengeluaran nya yaitu:'''

#Makan dan Transportasi pengurus sebesar Rp.1000000
#Hadiah untuk peserta sebesar Rp.1000000
#Sewa alat bahan dalam melakukan kegiatan perlombaan jumlah pengeluaran Rp1250000
#Carilah sisa dana dari pengeluaran untuk kegiatan perlombaan ini

Dana_makan_dan_minum=input('Masukan jumlah dana yang dikeluarkan untuk biaya makan dan transportasi pengurus :')
Dana_hadiah=input ('Masukan jumlah dana yang dikeluarkan untuk biaya hadiah peserta :')
Dana_sewa=input('Masukan jumlah dana yang akan dikeluarkan untuk sewa bahan dan alat :')

jumlah_awal_dana=350000
Dana_makan_dan_minum=1000000
Dana_hadiah=1000000
Dana_sewa=1250000

sisa_dana = (jumlah_awal_dana -Dana_makan_dan_minum -Dana_hadiah -Dana_sewa)
print('sisa dana dari kegiatan perlombaan ini yaitu:Rp',sisa_dana)
