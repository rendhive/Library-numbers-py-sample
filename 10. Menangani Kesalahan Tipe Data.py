import numbers

def divide(x, y):
    if not isinstance(y, numbers.Real) or y == 0:
        raise ValueError("Pembagi harus angka real dan tidak boleh nol.")
    return x / y

try:
    print(divide(10, 2))  # Valid
    print(divide(10, 0))  # Invalid
except ValueError as e:
    print("Kesalahan:", e)
# Fungsi: Membagi dua angka dengan validasi input.
# Kondisi: Ketika Anda ingin menghindari pembagian dengan nol.
