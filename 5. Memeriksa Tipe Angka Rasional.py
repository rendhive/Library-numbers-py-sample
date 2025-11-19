import numbers

from fractions import Fraction

num = Fraction(1, 2)

if isinstance(num, numbers.Rational):
    print("1/2 adalah pecahan rasional!")
# Fungsi: Memeriksa apakah sebuah objek adalah bilangan rasional.
# Kondisi: Ketika Anda bekerja dengan pecahan dan ingin diakui sebagai rasional.
