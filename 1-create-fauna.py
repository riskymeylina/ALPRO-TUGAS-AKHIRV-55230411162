import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

#CREATE TABLE FAUNA
koneksi.execute('''
                CREATE TABLE FAUNA(
                    id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_fauna VARCHAR(50),
                    jenis VARCHAR(50),
                    asal VARCHAR(50),
                    jml_sekarang INT(10),
                    thn_ditemukan INT(10)
                )
                ''')
koneksi.close()