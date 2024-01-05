# UPDATE data fauna jml_sekarang
import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

#Gunakan Query UPDATE SET
kursor.execute(f"UPDATE FAUNA SET jml_sekarang = '650'  WHERE nama_fauna = 'Katak Borneo' ")
koneksi.commit()

#CEK apakah data berhasil diubah atau belum
if kursor.rowcount > 0 : # cek berdasarkan adanya baris atau tidak
    print(f"Data fauna berhasil Diubah!")
else :
    print(f"Tidak ada data fauna!")
     

koneksi.close