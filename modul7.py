def bilangan(n):
    if n <= 1:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True

prima = float(input("Masukkan bilangan = "))

if bilangan(prima):
    print('Adalah bilangan prima')
else:
    print('Bukan bilangan prima')
    
#Latihan 2
def convert_to_ordinal(number):
    if 11 <= number <= 13:
        return f"{number}th"
    
    last_digit = number % 10
    if last_digit == 1:
        return f"{number}st"
    elif last_digit == 2:
        return f"{number}nd"
    elif last_digit == 3:
        return f"{number}rd"
    else:
        return f"{number}th"

def main():
    try:
        while True:
            user_input = int(input("Masukkan angka (0 untuk keluar): "))
            
            if user_input == 0:
                print("Program selesai")
                break
            
            ordinal_form = convert_to_ordinal(user_input)
            print(f"Angka: {user_input}")
            print(f"{ordinal_form}")
            
    except ValueError:
        print("Masukkan angka yang valid!")

if __name__ == "__main__":
    main()