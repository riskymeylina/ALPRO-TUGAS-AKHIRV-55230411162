# Filter karakter dataNAMA_FAUNA
import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()\

Nama = 'B%' 
kursor.execute(f"SELECT * FROM FAUNA WHERE nama_fauna LIKE ?", (Nama,))
baris_tabel = kursor.fetchall()

print("Tabel Fauna")
print("="*110)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID Fauna", "Nama Fauna", "Jenis", "Asal", "Jumlah Sekarang", "Tahun Ditemukan"))
print("-"*110)

for baris in baris_tabel :
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()




