def hitung_lembur(jam):
    if jam > 20:
        return  jam * 100000
    elif jam >= 11:
        return  jam * 75000
    elif jam >= 3:
        return  jam * 50000
    else:
        return 0 
def hitung_tunjangankeluarga(status, jumlahanak):
    if status == "k" or status == "K":
        return  jumlahanak * 100000
    else:
        return 0 
def main():
    nama = input("masukkan nama: ")
    golongan = input("masukkan golongan: A/B/C ")
    gaji_pokok = int(input("Masukkan gaji pokok: "))
    jam = int(input("Masukkan total jam lembur: "))
    status = input("status kawin: k = kawin T = tidak kawin ")
    jumlahanak = int(input("masukkan jumlah anak: "))

    lembur = hitung_lembur(jam)
    tunjangan = hitung_tunjangankeluarga(status, jumlahanak)
    total_kotor = gaji_pokok + lembur + tunjangan 
    pph = int(0.05 * total_kotor)
    gajibersih = total_kotor - pph

    print("Slip Gaji PT Ayunya Kamu")
    print("-"*30)
    print(f"Nama Karyawan         :{nama}")
    print(f"Golongan              :{golongan}")
    print(f"Gaji pokok            :{gaji_pokok}")
    print(f"Jumlah jam lembur     :{jam}")
    print(f"Status Kawin          :{status.upper()}")
    print(f"Total uang lembur     :{lembur}")
    print(f"Total uang tunjangan  :{tunjangan}")
    print(f"Total gaji kotor      :{total_kotor}")
    print(f"PPH                   :{pph}")
    print(f"Gaji Bersih           :{gajibersih}")

main()
