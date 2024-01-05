import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()


asal = 'Kalimantan'

kursor.execute(f"DELETE FROM FAUNA WHERE asal = ?", (asal,))
koneksi.commit()

#CEK apakah data berhasil diubah atau belum
if kursor.rowcount > 0 : # cek berdasarkan adanya baris atau tidak
    print(f"Data dari asal {asal} berhasil Dihapus!")
else :
    print(f"Tidak ada data fauna dari asal {asal}!")
    
#Putuskan Koneksi 
koneksi.close

