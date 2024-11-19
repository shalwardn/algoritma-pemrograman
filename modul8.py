#Latihan 1
def jumlah_rekursif(jumlah):
    if jumlah == 0:
        return 0
    angka = int(input(f"Masukkan angka ke-{jumlah}: "))
    return angka + jumlah_rekursif(jumlah - 1)

jumlah = int(input("Jumlah angka : "))
hasil = jumlah_rekursif(jumlah)
print("Hasil dari penjumlahan adalah :", hasil)

#Latihan 2
def pangkat(bilangan, p):
    if p == 0:
        return 1
    
    if p < 0:
        return 1 / (bilangan * pangkat(bilangan, abs(p) - 1))
    return bilangan * pangkat(bilangan, p - 1)

bilangan = int(input("Masukkan bilangan: "))
pangkat_input = int(input("Masukkan pangkat: "))

hasil = pangkat(bilangan, pangkat_input)
print(f"{bilangan} dipangkatkan {pangkat_input} adalah: {hasil}")