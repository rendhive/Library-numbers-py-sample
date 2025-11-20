import numbers

def print_number(num):
    if isinstance(num, numbers.Number):
        print("Angka:", num)
    else:
        print("Bukan angka.")

print_number(28)       # Angka
print_number(3.14)     # Angka
print_number("Hello")  # Bukan angka
# Fungsi: Mencetak angka yang valid.
# Kondisi: Ketika Anda ingin berbeda mengelola angka dan input lainnya.
