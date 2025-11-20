import numbers

def average(numbers_list):
    total = sum(num for num in numbers_list if isinstance(num, numbers.Number))
    count = len([num for num in numbers_list if isinstance(num, numbers.Number)])
    return total / count if count > 0 else 0

print("Rata-rata:", average([1, 2, 3, 4, 'a', 5.5]))  # Rata-rata dari angka
# Fungsi: Menghitung rata-rata semua angka dalam daftar.
# Kondisi: Ketika Anda perlu mendapatkan nilai tengah dari kumpulan angka.
