import numbers

def multiply(x, y):
    if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
        return x * y
    raise ValueError("Input harus berupa angka.")

print(multiply(5, 10))  # Mengalikan dua angka
# Fungsi: Fungsi yang mengalikan dua bilangan jika keduanya angka.
# Kondisi: Ketika Anda ingin melakukan perhitungan dengan validasi input.
