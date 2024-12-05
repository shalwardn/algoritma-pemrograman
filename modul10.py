#Latihan 1 - Shalwa Ridani
data = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
angka = int(input('Angka yang dicari: '))
print('Sebelum bubble sort:', data)

n = len(data)
for i in range(n - 1):
    for j in range(n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print('Hasil bubble sort:', data)

a = 0
b = len(data) - 1
found = False

while a <= b:
    j = (a + b) // 2
    if data[j] == angka:
        print('Elemen ditemukan di urutan ke-', j + 1)
        found = True
        break
    elif data[j] > angka:
        b = j - 1
    else:
        a = j + 1

if not found:
    print('Elemen tidak ditemukan.')

#Latihan 2 - Shalwa Ridani
def sort_data(data, n=None): #--- ini rekursifffff
    if n is None:
        n = len(data)
    if n == 1:
        return
    for i in range(n - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
    sort_data(data, n - 1)

def search_data(data, target, start, end): #--- ini rekursif juga
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return search_data(data, target, start, mid - 1)
    else:
        return search_data(data, target, mid + 1, end)

data = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
target = int(input("Masukkan angka yang dicari: "))
print("Data sebelum diurutkan:", data)

sort_data(data)
print("Data setelah diurutkan:", data)

result = search_data(data, target, 0, len(data) - 1)
if result != -1:
    print(f"Angka ditemukan pada urutan ke-{result + 1}")
else:
    print("Angka tidak ditemukan.")