# Mengurutkan sebuah data berdasarkan JML_SEKARANG dari yg terbanyak
import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()
#Mengambil semua data dalam tabel dan tampilan
kursor.execute("SELECT * FROM FAUNA ORDER BY jml_sekarang DESC ")
#Tampilkan dalam bentuk baris
baris_tabel = kursor.fetchall()
#Membuat format table dengan method format()
print("Tabel Fauna")
print("="*110)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID Fauna", "Nama Fauna", "Jenis", "Asal", "Jumlah Sekarang", "Tahun Ditemukan"))
print("-"*110)
#Tampilkan data sesuai format tabe dg perulangan
for baris in baris_tabel :
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()