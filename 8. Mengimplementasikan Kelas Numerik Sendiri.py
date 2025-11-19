import numbers

class MyNumber(numbers.Integral):
    def __init__(self, value):
        self._value = value

    def __int__(self):
        return self._value

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self._value + other._value)
        return NotImplemented

num1 = MyNumber(10)
num2 = MyNumber(5)
result = num1 + num2
print("Hasil penjumlahan:", result)
# Fungsi: Mengimplementasikan kelas numerik kustom untuk menggunakan tipe numerik.
# Kondisi: Ketika Anda mendefinisikan tipe angka yang khusus dalam aplikasi.
