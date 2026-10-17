nama = input("masukkan nama ")
gapok = int(input("Masukkan gaji pokok "))
tunjangan = int(input("Masukkan tunjangan anda "))
potongan = int(input("Masukkan potongan "))

bersih = gapok+tunjangan-potongan

print(f"Total gaji bersih anda adalah {bersih}")