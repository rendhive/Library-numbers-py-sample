import sqlite3
import matplotlib.pyplot as plt

# --- 1. Buat database SQLite in-memory ---
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# --- 2. Buat table penjualan ---
cur.execute("""
CREATE TABLE sales (
    month TEXT,
    sales INTEGER
)
""")

# --- 3. Masukkan data penjualan yang terus naik ---
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [1000 + i*300 for i in range(len(months))]  # penjualan naik tiap bulan

for m, s in zip(months, sales):
    cur.execute("INSERT INTO sales (month, sales) VALUES (?, ?)", (m, s))

conn.commit()

# --- 4. Ambil data dari SQL ---
cur.execute("SELECT month, sales FROM sales")
rows = cur.fetchall()

months_sql = [r[0] for r in rows]
sales_sql = [r[1] for r in rows]

# --- 5. Tampilkan grafik penjualan ---
plt.plot(months_sql, sales_sql, marker='o', color='blue')
plt.xlabel("Bulan")
plt.ylabel("Penjualan")
plt.title("Grafik Penjualan yang Terus Naik")
plt.grid(True)
plt.show()

# --- 6. Tutup koneksi ---
conn.close()