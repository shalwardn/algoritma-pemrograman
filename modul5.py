#Latihan 1
total_nilai = 0
jumlah_nilai = 0

while True:
    nilai = input('Masukkan nilai : ')
    
    if nilai == "":
        break
    nilai = nilai.upper()
    
    if nilai not in ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "E"]:
        print("Masukkan nilai dengan benar!")
    
    if nilai == "A":
        print("A = 4.00")
        total_nilai += 4.00
    elif nilai == "A-":
        print("A- = 3.75")
        total_nilai += 3.75
    elif nilai == "B+":
        print("B+ = 3.50")
        total_nilai += 3.50
    elif nilai == "B":
        print("B = 3.00")
        total_nilai += 3.00
    elif nilai == "B-":
        print("B- = 2.75")
        total_nilai += 2.75
    elif nilai == "C+":
        print("C+ = 2.50")
        total_nilai += 2.50
    elif nilai == "C":
        print("C = 2.00")
        total_nilai += 2.00
    elif nilai == "C-":
        print("C- = 1.75")
        total_nilai += 1.75
    elif nilai == "D":
        print("D = 1.50")
        total_nilai += 1.50
    elif nilai == "E":
        print("E = 1.25")
        total_nilai += 1.25
    else:
        print("Masukan nilai dengan benar!")
        
    jumlah_nilai += 1

if jumlah_nilai > 0:
    rata_rata = total_nilai / jumlah_nilai
    print(f"Rata - rata nilai : {rata_rata}")
else:
    print("Tidak ada nilai yang diinput")
    
#Latihan 2

total_harga = 0

print("=== Selamat Datang di Kebun Binatang Trisakti ===")
print("      Silahkan membeli tiket masuk disini ^^     ")
print("=================================================")

while True:
    umur = input('Umur : ')
    
    if umur == "":
        break
    
    umur = int(umur)
    
    if umur <= 2:
        print("Gratis")
        total_harga += 0
    elif 3 <= umur <= 12:
        print("harga : $14")
        total_harga += 14
    elif umur >= 65:
        print("harga : $18")
        total_harga += 18
    else:
        print("harga : $23")
        total_harga += 23

print("============ Kebun Binatang Trisakti ============")
print(f"Total harga : ${total_harga:.2f}")

pembayaran = float(input("Input uang : $"))

if pembayaran == total_harga:
    print(f"Pembayaran pas, terima kasih!")
else :
    kembalian = pembayaran - total_harga
    print(f"Kembalian anda : ${kembalian:.2f}")
    
print("=================================================")
print("Terima kasih telah berkunjung ke Kebun Binatang Trisakti ^^")