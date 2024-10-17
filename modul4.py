#Latihan 1
i = int(input("Masukkan angka: "))
for i in range(i, 0, -1):
    for loop in range(i):
        print(i, end='')
    print()
    
# Latihan 2
print("Masukkan angka di luar bulan (1-12) untuk berhenti")

while True:
    bulan = input("Bulan (1-12): ")
    
    try:
        bulan = int(bulan)
    except ValueError:
        print("Input tidak valid, silakan masukkan angka.")
        continue

    if bulan < 1 or bulan > 12:
        print("Byeeee")
        break

    if bulan == 2:
        tahun = input("Masukkan tahun: ")
        
        try:
            tahun = int(tahun)
        except ValueError:
            print("Input tahun tidak valid, silakan masukkan angka.")
            continue
    
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            print("Ada 29 hari (tahun kabisat).")
        else:
            print("Ada 28 hari.")
    elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        print("Ada 31 hari.")
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        print("Ada 30 hari.")