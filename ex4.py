mobil = 100
ruang_dalam_mobil = 4.0
pengemudi = 30
penumpang = 90
mobil_yang_tdk_dikemudikan = mobil - pengemudi
mobil_yang_dikemudikan = pengemudi
kapasitas_mobil = mobil_yang_dikemudikan * ruang_dalam_mobil
rerata_penumpang_per_mobil = penumpang / mobil_yang_dikemudikan

print ("ada ", mobil, " mobil yang tersedia")
print ("ada ", pengemudi, " pengemudi yang tersedia")
print ("ada ", mobil_yang_tdk_dikemudikan, " mobil yang kosong saat ini")
print ("kami dapat mengantarkan ", kapasitas_mobil, " orang saat ini")
print ("kami memiliki ", penumpang, " penumpang saat ini")
print ("rata-rata penumpang per mobil saat ini yaitu ", rerata_penumpang_per_mobil, " untuk setiap mobilnya")