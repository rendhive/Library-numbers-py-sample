import numbers

def check_number(n):
    if isinstance(n, numbers.Number):
        return True
    return False

print(check_number(10))  # Angka
print(check_number(3.5))  # Float
print(check_number('abc'))  # String
# Fungsi: Memeriksa setiap tipe yang diturunkan dari Number.
# Kondisi: Ketika Anda melakukan fungsi generik untuk angka.
