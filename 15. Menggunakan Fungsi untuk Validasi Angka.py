import numbers

def validate_number(num):
    if not isinstance(num, numbers.Number):
        raise TypeError("Input harus angka.")
    return num

try:
    validate_number("123")  # Akan memicu kesalahan
except TypeError as e:
    print("Kesalahan:", e)
# Fungsi: Memvalidasi bahwa input adalah angka.
# Kondisi: Kebijakan untuk memastikan input yang valid dalam aplikasi.
