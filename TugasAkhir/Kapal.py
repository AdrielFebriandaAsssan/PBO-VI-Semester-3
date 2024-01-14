import mysql.connector
from koneksi import koneksi, tutup_koneksi

connection = koneksi()
cursor = connection.cursor()

class Kapal():
    def __init__(self, connection):
        self._connection = connection
        self._cursor =  connection.cursor()

    def _NyaladanMatikanKoneksi(self):
        self._connection.commit()
        tutup_koneksi(self._connection, self._cursor)    
    

    def input_kapal(self, Nama_Kapal, Asal_Negara, Tipe, Class, Tahun_Ditugaskan):
        self._cursor.execute('''INSERT INTO kapalperang 
            (Nama_Kapal, Asal_Negara, Tipe, Class, Tahun_Ditugaskan)
            VALUES (%s, %s, %s, %s, %s)''' ,(Nama_Kapal, Asal_Negara, Tipe, Class, Tahun_Ditugaskan))
        self._NyaladanMatikanKoneksi()
        print("Berhasil Ditambahkan :3")
        return self._cursor.lastrowid

    def get_kapal(self):
        self._cursor.execute("SELECT * FROM kapalperang")
        return self._cursor.fetchall()


    def delete_kapal(self, id_kapal):
        try:
            self._cursor.execute("DELETE FROM kapalperang WHERE id_kapal = %s", (id_kapal,))
            self._NyaladanMatikanKoneksi()
            print("Data Kapal Berhasi Dihapus UwU")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def show_kapal(self):
        try:
            self._cursor.execute("SELECT * FROM kapalperang")
            rows = self._cursor.fetchall()

            if not rows:
                print("Data Kosong >:(")
            else:
                print("Daftar Kapal:")
                for row in rows:
                    print(f'''
                    ID Kapal: {row[0]}, Nama Kapal: {row[1]}, 
                    Asal Negara: {row[2]}, Tipe Kapal: {row[3]}, 
                    Kelas Kapal: {row[4]}, Tahun Diluncurkan: {row[5]}''')
                    
        except mysql.connector.Error as err:
            print(f"Error: {err}")

class Komandan(Kapal):
    def __init__(self, connection):
        super().__init__(connection)

    def input_komandan(self, Nama_Komandan, Pangkat, Tahun_Dinas, id_kapal):
        try:
            # Check if the provided id_kapal exists in the kapalperang table
            self._cursor.execute("SELECT id_kapal FROM kapalperang WHERE id_kapal = %s", (id_kapal,))
            daftar_kapal = self._cursor.fetchone()

            if daftar_kapal:
                self._cursor.execute('''
                    INSERT INTO komandan 
                    (Nama_Komandan, Pangkat, Tahun_Dinas, id_kapal)
                    VALUES (%s, %s, %s, %s)
                ''', (Nama_Komandan, Pangkat, Tahun_Dinas, id_kapal))
                print("Berhasil Ditambahkan :3")
                self._NyaladanMatikanKoneksi()
            else:
                print(f"Error: Kapal Dengan ID {id_kapal} Tidak Ada >:(")
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def get_komandan(self, id_kapal):
        self._cursor.execute('SELECT * FROM komandan WHERE id_kapal = %s', (id_kapal,))
        return self._cursor.fetchall()


    def delete_komandan(self, id_komandan):
        try:
            self._cursor.execute("DELETE FROM Komandan WHERE id_komandan = %s", (id_komandan,))
            self._NyaladanMatikanKoneksi()
            print("Data Komandan Berhasil Di Hapus")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
    def show_komandan(self):
        try:
            self._cursor.execute("SELECT * FROM komandan")
            rows = self._cursor.fetchall()
            if not rows:
                print("Data Kosong >:(")
            else:
                print("Daftar Komandan:")
                for row in rows:
                    print(f'''
                    ID Komandan: {row[0]}, Nama Komandan: {row[1]}, 
                    Pangkat: {row[2]}, Tahun Dinas: {row[4]}, 
                    ID Kapal: {row[3]}''')

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    
    def tampil_kapal(self):
        try:
            self._cursor.execute("SELECT * FROM kapalperang")
            rows = self._cursor.fetchall()

            if not rows:
                print("Data Kosong >:(")
            else:
                print("Daftar Kapal:")
                for row in rows:
                    print(f'''
                    ID Kapal: {row[0]}, Nama Kapal: {row[1]}''')
                    
        except mysql.connector.Error as err:
            print(f"Error: {err}")

            
    def __str__(self):
        return "Tester"

class Pertempuran(Kapal):
    def __init__(self, connection):
        super().__init__(connection)

    def input_pertempuran(self, Nama_Pertempuran, Tanggal_Pertempuran, Lokasi, Hasil_Pertempuran, id_kapal, id_komandan):
        self._cursor.execute('''
        INSERT INTO pertempuran
        (Nama_Pertempuran, Tanggal_Pertempuran, Lokasi, Hasil_Pertempuran, id_kapal, id_komandan)
        VALUES (%s, %s, %s, %s, %s, %s)
        ''', (Nama_Pertempuran, Tanggal_Pertempuran, Lokasi, Hasil_Pertempuran, id_kapal, id_komandan))
        print("Pertempuran Berhasil Di Tambahkan UwU ")
        self._NyaladanMatikanKoneksi()

    def _select_pertempuran(self):
        PertempuranPenting = self._get_Pertempuran()
        print("\nDaftar Pertempuran:")
        for battle in PertempuranPenting:
            print(f"id_pertempuran: {battle[0]}, Nama_Pertempuran: {battle[1]}, Tanggal_Pertempuran: {battle[2]}")

        id_tempur = input("Masukan id_pertempuran: ")
        return int(id_tempur) if id_tempur.isdigit() else None

    def _get_Pertempuran(self):
        self._cursor.execute('SELECT * FROM pertempuran')
        return self._cursor.fetchall()



    def delete_kapal(self, id_kapal):
        try:
            self._cursor.execute("DELETE FROM kapalperang WHERE id_kapal = %s", (id_kapal,))
            self._NyaladanMatikanKoneksi()
            print("Data Kapal Berhasi Dihapus UwU")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def show_pertempuran(self):
        try:
            self._cursor.execute("SELECT * FROM pertempuran")
            rows = self._cursor.fetchall()
            if not rows:
                print("Data Kosong >:(")
            else:
                print("Daftar Komandan:")
                for row in rows:
                    print(f'''
                    ID Pertempuran: {row[0]}, Nama Pertempuran: {row[1]}, 
                    Tanggal Pertempuran: {row[2]}, Lokasi: {row[3]}, 
                    Hasil Pertempuran: {row[4]}, ID Kapal: {row[5]}, ID Komandan: {row[6]}''')

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def __str__(self):
        return "Pertempuran class for managing Pertempurans involving historical Kapals."

class Korban(Pertempuran):
    def __init__(self, connection):
        super().__init__(connection)

    def input_Korban(self, id_pertempuran, id_kapal, Tipe_Korban, JumlahKorban):
        self._cursor.execute('''
        INSERT INTO pertempuran
        (id_pertempuran, id_kapal, Tipe_Korban, JumlahKorban)
        VALUES (%s, %s, %s, %s)
        ''', (id_pertempuran, id_kapal, Tipe_Korban, JumlahKorban))
        print("Pertempuran Berhasil Di Tambahkan UwU ")
        self._NyaladanMatikanKoneksi()

   
    def delete_korban(self, id_korban):
        try:
            self._cursor.execute("DELETE FROM korbanjiwa WHERE id_korban = %s", (id_korban,))
            self._NyaladanMatikanKoneksi()
            print("Data Korban Berhasil Di Hapus UwU")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def show_korbanjiwa(self):
        try:
            self._cursor.execute("SELECT * FROM korbanjiwa")
            rows = self._cursor.fetchall()
            if not rows:
                print("Data Kosong >:(")
            else:
                print("Daftar Korban:")
                for row in rows:
                    print(f'''
                    ID Korban: {row[0]}, ID Pertempuran: {row[1]}, 
                    ID Kapal: {row[2]}, Tipe Korban: {row[3]}, 
                    Jumlah Korban: {row[4]}''')

        except mysql.connector.Error as err:
            print(f"Error: {err}")

while True:
    print("\n===== Main Menu =====")
    print("1. kapal Menu")
    print("2. komandan Menu")
    print("3. pertempuran Menu")
    print("4. korban Menu")
    print("5. Exit")

    main_pilih = input("Masukan Pilihan Mu :3 (1-5): ")

    if main_pilih == '1':
        
        while True:
            print("\n===== kapal Menu =====")
            print("1. Tambah kapal")
            print("2. Delete kapal")
            print("3. Show kapal")
            print("4. Back to Main Menu")

            kapal_pilih = input("Masukan Pilihan Mu :3 (1-5): ")

            if kapal_pilih == '1':
                kapal = Kapal(koneksi())
                kapal.input_kapal(
                    input("Masukan Nama kapal: "),
                    input("Masukan Asal Negara: "),
                    input("Masukan Tipe kapal: "),
                    input("Masukan Class kapal: "),
                    int(input("Masukan Tahun_Ditugaskan: "))
                )
    
            elif kapal_pilih == '2':
                kapal = Kapal(koneksi())
                id_kapal = input("Masukan ID Kapal Yang Ingin DI Hapus ")
                kapal.delete_kapal(id_kapal)

            elif kapal_pilih == '3':
                kapal = Kapal(koneksi())
                kapal.show_kapal()
            elif kapal_pilih == '4':
                break
            else:
                print("Plihan Tidak Valid. Masukan Nomor Antara 1-4.")

    elif main_pilih == '3':
      
        while True:
            print("\n===== Pertempuran Menu =====")
            print("1. Tambah Pertempuran")
            print("2. Delete Pertempuran")
            print("3. Show Pertempurans")
            print("4. Back to Main Menu")

            pertempuran_pilih = input("Masukan Pilihan Mu :3 (1-4): ")

            if pertempuran_pilih == '1':
                pertempuran = Pertempuran(koneksi())
                pertempuran.input_pertempuran(
                    input("Masukan Nama Pertempuran: "),
                    input("Masukan Tanggal Pertempuran: "),
                    input("Masukan Lokasi Pertempuran: "),
                    input("Masukan Hasil Pertempuran: "),
                    input("Masukan ID Kapal: "),
                    input("Masukan ID Komandan: "),
                )
            elif pertempuran_pilih == '2':
                pertempuran = Pertempuran(koneksi())
                id_pertempuran = input("Masukan ID Pertempuran Yang Ingin Di Hapus :3 ")
                pertempuran.delete_pertempuran(id_pertempuran)

            elif pertempuran_pilih == '3':
                pertempuran = Pertempuran(koneksi())
                pertempuran.show_pertempurans()
            elif pertempuran_pilih == '4':
                break
            else:
                print("Plihan Tidak Valid. Masukan Nomor Antara 1-4.")

    elif main_pilih == '4':
        
        while True:
            print("\n===== korban Menu =====")
            print("1. Tambah korban")
            print("2. Delete korban")
            print("3. Show korban")
            print("4. Back to Main Menu")

            korban_pilih = input("Masukan Pilihan Mu :3 (1-4): ")

            if korban_pilih == '1':
                korban = Korban(koneksi())
                korban.input_Korban(
                    input("Masukan ID Pertempuran: "),
                    input("Masukan ID Kapal: "),
                    input("Masukan Tipe Korban: "),
                    input("Masukan Jumlah Korban: ")
                )
            elif korban_pilih == '2':
                korban = Korban(koneksi())
                id_korban = input("Masukan ID Korban Yang Ingin Di Hapus ")
                korban.delete_korban(id_korban)
            elif korban_pilih == '3':
                korban = Korban(koneksi())
                korban.show_korbanjiwa()
            elif korban_pilih == '4':
                break
            else:
                print("Plihan Tidak Valid. Masukan Nomor Antara 1-4.")
    elif main_pilih == '2':
     
        while True:
            print("\n===== Komandan Menu =====")
            print("1. Tambah Komandan")
            print("2. Delete Komandan")
            print("3. Show Komandans")
            print("4. Back to Main Menu")

            Komandan_pilih = input("Masukan Pilihan Mu :3 (1-4): ")

            if Komandan_pilih == '1':
                komandan = Komandan(koneksi())
                komandan.tampil_kapal()
                komandan.input_komandan(
                    input("Masukan Nama Komandan: "),
                    input("Masukan Pangkat Komandan: "),
                    input("Masukan Tahun Berdinas: "),
                    input("Masukan ID Kapal Dinas: ")
                )
            elif Komandan_pilih == '2':
                komandan = Komandan(koneksi())
                id_komandan = input("Masukan ID Komandan Yang Ingin Di Hapus: ")
                komandan.delete_komandan(id_komandan)
            elif Komandan_pilih == '3':
                komandan = Komandan(koneksi())
                komandan.show_komandan()
            elif Komandan_pilih == '4':
                break
            else:
                print("Plihan Tidak Valid. Masukan Nomor Antara 1-4.")

    elif main_pilih == '5':
        print("Goodbye JoJo, WRYYYYYYYYY")
        break

    else:
        print("Plihan Tidak Valid. Masukan Nomor Antara 1-5.")