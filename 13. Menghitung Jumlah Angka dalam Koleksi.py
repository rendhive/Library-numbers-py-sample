import numbers

def sum_numbers(numbers_list):
    return sum(num for num in numbers_list if isinstance(num, numbers.Number))

numbers_list = [1, 2.5, 'a', 3, 4.5]
total = sum_numbers(numbers_list)
print("Jumlah semua angka dalam daftar:", total)
# Fungsi: Menghitung jumlah dari semua angka dalam daftar.
# Kondisi: Ketika Anda menganalisis kumpulan data yang mungkin berisi tipe yang berbeda.
