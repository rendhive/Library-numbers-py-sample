import numbers

def power(num, exp):
    if isinstance(num, numbers.Real) and isinstance(exp, numbers.Integral):
        return num ** exp
    raise ValueError("Input harus angka real dan eksponen harus integer.")

print(power(2, 3))  # 8
print(power(3.0, 2))  # 9.0
# Fungsi: Menghitung pangkat dari angka dengan validasi tipe.
# Kondisi: Ketika Anda melakukan operasi eksponen pada angka.
