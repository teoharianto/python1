import ex40a
import ex40b

while True:
    call = ex40b.MyClass()
    call.pertanyaan()
    try:
        angka1s = int(ex40b.MyClass.angka1)
        angka2s = int(ex40b.MyClass.angka2)
    except ValueError:
        print("Angka anda tidak valid")
        print("-" * 10)
        continue
    
    hasil = ex40a.MyClassChild(angka1s, angka2s)

    print("hasil penjumlahan adalah :", hasil.penjumlahan())
    print("hasil pengurangan adalah :", hasil.pengurangan())

    break
