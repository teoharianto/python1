# Berikut adalah kode yang menerima inputan

print ("Siapa Nama Kamu ? ", end='')
nama = input()

print ("Kamu lahir dimana ? ", end='')
tempat_lahir = input()

print ("Kamu umur berapa ? ", end='')
umur = int(input()) # Convert String Ke Integer

print(f"Jadi nama kamu {nama}, dan kamu lahir di {tempat_lahir}, dan umur kamu {umur}.")
print(umur + 2) # Penjumlahan nilai yang telah di convert ke Integer