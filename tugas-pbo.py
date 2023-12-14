class KendaraanDarat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.tahun_keluaran = tahun_keluaran
        self.nama = nama
        self.warna = warna
        self.kecepatan = kecepatan
        self.bahan_bakar = bahan_bakar
        self.jumlah_roda = jumlah_roda
        self.kapasitas_penumpang = kapasitas_penumpang

    def __str__(self):
        return f"{self.nama} ({self.tahun_keluaran}), Warna: {self.warna}, Kecepatan: {self.kecepatan} km/h, Bahan Bakar: {self.bahan_bakar}, Jumlah Roda: {self.jumlah_roda}, Kapasitas Penumpang: {self.kapasitas_penumpang}"

class Kereta(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.gerbong = 0
        self.jumlah_kursi = 0
        self.jenis_layanan_kereta = ""
        self.rute = []

    def tambah_rute(self, rute):
        self.rute.append(rute)

    def kurangi_rute(self, rute):
        if rute in self.rute:
            self.rute.remove(rute)

    def __str__(self):
        return f"{super().__str__()}, Gerbong: {self.gerbong}, Jumlah Kursi: {self.jumlah_kursi}, Jenis Layanan Kereta: {self.jenis_layanan_kereta}, Rute: {', '.join(self.rute)}"

class Mobil(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_mobil = jenis_mobil

    def start_engine(self):
        return "Mesin dinyalakan."

    def stop_engine(self):
        return "Mesin dimatikan."

    def maju(self):
        return "Mobil bergerak maju."

    def mundur(self):
        return "Mobil mundur."

    def belok(self):
        return "Mobil belok."

    def __str__(self):
        return f"{super().__str__()}, Jenis Mobil: {self.jenis_mobil}"

class MobilBalap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil="Balap")
        self.front_wing = 0
        self.rear_wing = 0

    def race(self):
        return "Mobil balap sedang berlomba."

    def __str__(self):
        return f"{super().__str__()}, Front Wing: {self.front_wing}, Rear Wing: {self.rear_wing}"

class MobilCrossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil="Offroad")
        self.sunroof_type = ""
        self.shock_breaker = ""

    def sunroof_terbuka(self):
        return "Sunroof terbuka."

    def sunroof_tertutup(self):
        return "Sunroof tertutup."

    def __str__(self):
        return f"{super().__str__()}, Sunroof Type: {self.sunroof_type}, Shock Breaker: {self.shock_breaker}"

def main():
    # Objek Kereta
    kereta_api = Kereta(2022, "Kereta Api Ekspres", "Merah", 120, "Solar", 16, 200)
    kereta_api.tambah_rute("Jakarta - Surabaya")
    kereta_api.tambah_rute("Surabaya - Yogyakarta")
    kereta_api.kurangi_rute("Surabaya - Yogyakarta")

    # Objek MobilBalap
    mobil_balap = MobilBalap(2023, "Ferrari", "Merah", 300, "Bensin", 4, 2)
    mobil_balap.front_wing = 1
    mobil_balap.rear_wing = 1

    # Objek MobilCrossroad
    mobil_crossroad = MobilCrossroad(2021, "SUV Offroad", "Hitam", 150, "Bensin", 4, 5)
    mobil_crossroad.sunroof_type = "Panorama"
    mobil_crossroad.shock_breaker = "Adjustable"

    while True:
        print("\nPilihan Tindakan:")
        print("1. Informasi Kendaraan")
        print("2. Informasi Mobil Balap")
        print("3. Informasi Mobil Crossroad")
        print("4. Keluar")

        choice = input("Masukkan pilihan (1-4): ")

        if choice == "1":
            print("\nInformasi Kendaraan:")
            print(str(kereta_api))
        elif choice == "2":
            print("\nInformasi Mobil Balap:")
            print(str(mobil_balap))
        elif choice == "3":
            print("\nInformasi Mobil Crossroad:")
            print(str(mobil_crossroad))
        elif choice == "4":
            print("Terima kasih. Program berakhir.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
