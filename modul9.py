#Latihan 1
nama = input("Nama : ")
umur = input("Umur : ")
alamat = input("Alamat : ")
email = input("Email : ")
dosen = input("Dosen Wali : ")

teks = "\nNama : {}\nUmur : {}\nAlamat : {}\nEmail : {}\nDosen Wali : {}".format(nama, umur, alamat, email, dosen)
file_bio = open("test.txt", "w")
file_bio.write(teks)
file_bio.close()

file = open("test.txt", "r")
text = file.read()
print("\nBerikut data kamu")
print(text)
file.close()

#Latihan 2
def create_file():
    filename = input("Masukkan nama file: ").strip()
    name = input("Masukkan nama Anda: ").strip()
    nim = input("Masukkan NIM Anda: ").strip()
    year = input("Masukkan tahun angkatan: ").strip()

    file_content = (
        f"Informasi Pengguna\n"
        f"Nama File       : {filename}\n"
        f"Nama Anda       : {name}\n"
        f"NIM Anda        : {nim}\n"
        f"Tahun Angkatan  : {year}\n"
    )

    try:
        with open(filename, "w") as file:
            file.write(file_content)
        print(f"\nFile '{filename}' berhasil dibuat!\n")
    except Exception as e:
        print(f"\nTerjadi kesalahan saat membuat file: {e}\n")


def read_file():
    filename = input("Masukkan nama file: ").strip()
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"\n Isi File '{filename}' \n{content}\n")
    except FileNotFoundError:
        print(f"\nFile '{filename}' tidak ditemukan.\n")
    except Exception as e:
        print(f"\nTerjadi kesalahan saat membaca file: {e}\n")


def append_to_file():
    filename = input("Masukkan nama file: ").strip()
    name = input("Masukkan nama sahabat: ").strip()
    note = input("Masukkan catatan tambahan: ").strip()

    file_content = (
        f"Tambahan Informasi\n"
        f"Nama Sahabat   : {name}\n"
        f"Catatan        : {note}\n"
    )

    try:
        with open(filename, "a") as file:
            file.write(file_content)
        print(f"\nTeks berhasil ditambahkan ke file '{filename}'.\n")
    except Exception as e:
        print(f"\nTerjadi kesalahan saat menambahkan teks ke file: {e}\n")

def main():
    while True:
        print("\n========== Menu File Handling ==========")
        print("1. Buat File Baru")
        print("2. Baca File")
        print("3. Tambah Teks ke File")
        print("4. Keluar")
        print("========================================")
        
        choice = input("Pilih menu (1/2/3/4): ").strip()

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            append_to_file()
        elif choice == "4":
            print("\nTerima kasih telah menggunakan program ini. Bye Bye! :)")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.\n")

main()