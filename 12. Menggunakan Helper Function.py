import numbers

def is_numeric(val):
    return isinstance(val, numbers.Number)

print(is_numeric(1234))  # True
print(is_numeric(12.34))  # True
print(is_numeric("hello"))  # False
# Fungsi: Memeriksa apakah nilai adalah angka.
# Kondisi: Ketika Anda perlu memvalidasi input.
