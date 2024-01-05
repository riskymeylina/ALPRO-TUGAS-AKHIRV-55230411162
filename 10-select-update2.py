# UPDATE data fauna asal 
import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

#Gunakan Query UPDATE SET
kursor.execute(f"UPDATE FAUNA SET asal = 'Kalimantan Timur'  WHERE nama_fauna = 'Pesut Mahakam' ")
koneksi.commit()

#CEK apakah data berhasil diubah atau belum
if kursor.rowcount > 0 : # cek berdasarkan adanya baris atau tidak
    print(f"Data fauna berhasil Diubah!")
else :
    print(f"Tidak ada data fauna!")
     
koneksi.close