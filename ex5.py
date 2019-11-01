mobil = 100
ruang_dalam_mobil = 4.0
pengemudi = 30
penumpang = 90
mobil_yang_tdk_dikemudikan = mobil - pengemudi
mobil_yang_dikemudikan = pengemudi
kapasitas_mobil = mobil_yang_dikemudikan * ruang_dalam_mobil
rerata_penumpang_per_mobil = penumpang / mobil_yang_dikemudikan

print (f"ada {mobil} mobil yang tersedia")
print (f"ada {pengemudi} pengemudi yang tersedia")
print (f"ada {mobil_yang_tdk_dikemudikan} mobil yang kosong saat ini")
print (f"kami dapat mengantarkan {kapasitas_mobil} orang saat ini")
print (f"kami memiliki {penumpang} penumpang saat ini")
print (f"rata-rata penumpang per mobil saat ini yaitu {rerata_penumpang_per_mobil} untuk setiap mobilnya")

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_height_cm = round(my_height / 0.3937)
my_weight_kg = round(my_weight / 2.205)
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

total = my_age + my_height + my_weight
print (f"jadi zed berumur {my_age}, dan memiliki tinggi {my_height_cm} centimeter, serta memiliki berat {my_weight_kg} kilogram, sehingga bila di \ntotal keseluruhan jumlah yaitu {total}")