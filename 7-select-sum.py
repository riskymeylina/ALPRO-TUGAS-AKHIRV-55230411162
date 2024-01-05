# Menjumlahkan isian field JML_SEKARANG
import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()
# Ambil data berdasarkan 
kursor.execute("SELECT SUM(jml_sekarang) FROM FAUNA")
total= kursor.fetchone()[0] 

print(f"Total Populasi : {total}")

koneksi.close()