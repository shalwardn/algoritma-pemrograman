#Latihan 1
def rata_rata(nilaiA, nilaiC):
    hasil = (nilaiA + nilaiC) / 2
    return hasil

nilaiA = float(input("Nilai A : "))
nilaiC = float(input("Nilai C : "))

print("Rata-ratanya adalah:", rata_rata(nilaiA, nilaiC))

#Latihan 2
def input_bulan():
    while True:
        bulan = input("Bulan (1-12): ")
        try:
            bulan = int(bulan)
            if 1 <= bulan <= 12:
                return bulan
            else:
                print("Byeeee")
                return None
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")
           
def input_tahun():
    while True:
        tahun = input("Masukkan tahun: ")
        try:
            return int(tahun)
        except ValueError:
            print("Input tahun tidak valid, silakan masukkan angka.")
             
def hitung_hari(bulan, tahun=None):
    if bulan == 2:
        if tahun is not None:
            if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
                return "Ada 29 hari (tahun kabisat)."
            else:
                return "Ada 28 hari."
        else:
            return "Ada 28 atau 29 hari, tergantung tahun."
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return "Ada 31 hari."
    elif bulan in [4, 6, 9, 11]:
        return "Ada 30 hari."

def semua():
    print("Masukkan angka di luar bulan (1-12) untuk berhenti")
    
    while True:
        bulan = input_bulan()
        if bulan is None:
            break
        if bulan == 2:
            tahun = input_tahun()
            print(hitung_hari(bulan, tahun))
        else:
            print(hitung_hari(bulan))

semua()