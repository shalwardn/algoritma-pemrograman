#Latihan 1 - Shalwa Ridani
class Mahasiswa:
    empCount = 0
    
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.empCount += 1
    
    def displayCount(self):
        print ("Total Mahasiswa %d" % Mahasiswa.empCount)

    def biodata (self):
        print("\nNama anda : ", self.nama, "\nNIM anda : ", self.nim, "\nAngkatan anda : ", self.angkatan)

def main():
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            angkatan = int(input("Masukkan angkatan mahasiswa: "))
            
            mahasiswa = Mahasiswa(nama, nim, angkatan)
            mahasiswa.biodata()
            mahasiswa.displayCount()
            
main()

#Latihan 2 - Shalwa Ridani
class Programwow:
    def __init__(self):
        self.__name = None
        self.__value = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def delete_data(self):
        self.__name = None
        self.__value = None


def main():
    program_instance = Programwow()  # Ganti nama variabel

    while True:
        print("\n=========Program OOP=========")
        print("1. Deklarasi Data")
        print("2. Menampilkan Data")
        print("3. Mengubah Data")
        print("4. Menghapus Data")
        print("5. Keluar Aplikasi")

        try:
            choice = int(input("Masukkan pilihan (1/2/3/4/5): "))
        except ValueError:
            print("Input tidak valid. Masukkan angka 1-5.")
            continue

        if choice == 1:
            name = input("Masukkan nama: ")
            try:
                value = int(input("Masukkan nilai: "))
            except ValueError:
                print("Nilai harus berupa angka.")
                continue
            program_instance.set_name(name)
            program_instance.set_value(value)
            print("Data berhasil dideklarasikan.")

        elif choice == 2:
            name = program_instance.get_name()
            value = program_instance.get_value()
            print(f"Nama: {name if name else 'None'}")
            print(f"Nilai: {value if value else 'None'}")

        elif choice == 3:
            if program_instance.get_name() is None and program_instance.get_value() is None:
                print("Tidak ada data untuk diubah.")
                continue
            field = input("Apa yang ingin diubah? (Nama/Nilai): ").strip().lower()
            if field == "nama":
                new_name = input("Masukkan nama baru: ")
                program_instance.set_name(new_name)
                print("Nama berhasil diubah.")
            elif field == "nilai":
                try:
                    new_value = int(input("Masukkan nilai baru: "))
                except ValueError:
                    print("Nilai harus berupa angka.")
                    continue
                program_instance.set_value(new_value)
                print("Nilai berhasil diubah.")
            else:
                print("Input tidak valid.")

        elif choice == 4:
            program_instance.delete_data()
            print("Data berhasil dihapus.")

        elif choice == 5:
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")

main()