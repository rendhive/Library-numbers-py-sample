import numbers

def square(num):
    if not isinstance(num, numbers.Number):
        raise ValueError("Input harus angka.")
    return num * num

print("Kuadrat dari 3:", square(3))  # 9
print("Kuadrat dari 4.5:", square(4.5))  # 20.25
# Fungsi: Menghitung kuadrat dari sebuah angka.
# Kondisi: Ketika Anda ingin mengaplikasikan operasi matematis dasar pada angka.
