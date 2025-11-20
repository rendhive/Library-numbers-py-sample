import numbers

from fractions import Fraction

class CustomFraction(Fraction):
    def is_greater_than_one(self):
        return self > 1

frac = CustomFraction(5, 4)
print("Apakah 5/4 lebih besar dari 1?", frac.is_greater_than_one())
# Fungsi: Menciptakan subclass dari Fraction yang memiliki metode tambahan.
# Kondisi: Ketika Anda ingin memperluas fungsionalitas kelas yang ada.
