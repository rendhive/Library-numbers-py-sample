import numbers

class NumberContainer:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, num):
        if isinstance(num, numbers.Number):
            self.numbers.append(num)

container = NumberContainer()
container.add_number(10)
container.add_number(3.14)
print("Isi container:", container.numbers)
# Fungsi: Menyimpan angka dalam kelas khusus.
# Kondisi: Ketika Anda perlu mengelola koleksi angka.
