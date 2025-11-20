import numbers

def compare(num1, num2):
    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
        if num1 < num2:
            return f"{num1} lebih kecil dari {num2}"
        elif num1 > num2:
            return f"{num1} lebih besar dari {num2}"
        else:
            return "Keduanya sama."
    raise ValueError("Input harus angka.")

print(compare(10, 15))  # 10 lebih kecil dari 15
# Fungsi: Membandingkan dua angka dan mengembalikan hasil perbandingan.
# Kondisi: Saat Anda perlu melakukan evaluasi terhadap dua nilai numerik.
