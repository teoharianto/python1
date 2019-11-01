Pabrikan_Asia = ['Honda', 'Kawasaki', 'Yamaha']
Seri_Motor_Asia = {'Honda' : 'CBR', 'Kawasaki' : 'ZX', 'Yamaha' : 'YZF'}
Detail_Seri_Motor_Asia = {'CBR' : 'CBR500R, CBR1000RR', 'ZX' : 'ZX-10RR, ZX-14, H2', 'YZF' : 'YZF-R1, YZF-R6'}

Pabrikan_Eropa = ['Ducati', 'MV Augusta', 'Aprilia']
Seri_Motor_Eropa = {'Ducati' : 'Panigale', 'MV Augusta' : 'Brutale', 'Aprilia' : 'RSV4'}
Detail_Seri_Motor_Eropa = {'Panigale' : '959 Panigale Corse, Panigale V4', 'Brutale' : '1000 Serie ORO, 800 RR LH44, 800RC', 'RSV4' : 'RSV4 1100 Factory, RSV4 RR'}


# prompt = "> "

# print("Daftar motor pabrikan Asia atau Eropa ? (Isi Asia atau Eropa)")
# pabrikan = input(prompt)
# if pabrikan == "Asia" or pabrikan == "asia" :
#     for i in Pabrikan_Asia:
#         print (f"{i} punya tipe motor : {Detail_Seri_Motor_Asia[Seri_Motor_Asia[i]]}")
# elif pabrikan == "Eropa" or pabrikan == "eropa" :
#     for i in Pabrikan_Eropa:
#         print (f"{i} punya tipe motor : {Detail_Seri_Motor_Eropa[Seri_Motor_Eropa[i]]}")
# else :
#     print ("Tidak ada daftar sesuai permintaan anda !")

prompt = "> "

print("Daftar motor pabrikan Asia atau Eropa ? (Isi Asia atau Eropa)")
pabrikan = input(prompt)

if pabrikan == "Asia" or pabrikan == "asia" :
    for i,f in list(Seri_Motor_Asia.items()):
        print (f"{i} punya seri motor : {Detail_Seri_Motor_Asia[f]}")

elif pabrikan == "Eropa" or pabrikan == "eropa" :
    for i,f in list(Seri_Motor_Eropa.items()):
        print (f"{i} punya tipe motor : {Detail_Seri_Motor_Eropa[f]}")
else :
    print ("Tidak ada daftar sesuai permintaan anda !")
