def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)
    return nilai_akhir

data_siswa = []

while True:
    nama = input("Masukkan Nama siswa: ")
    nim = input("Masukkan NIM siswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = hitung_nilai(tugas, uts, uas)

    data_siswa.append({
        'Nama': nama,
        'NIM': nim,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    })

    tambah_data = input("Tambah data lagi? (y/t): ")
    if tambah_data.lower() != 'y':
        break

print("\nDaftar Data Siswa:")
print("===================================================================")
print("No.  Nama\tNIM\t\tTugas\tUTS\tUAS\tNilai Akhir")
print("===================================================================")
for idx, siswa in enumerate(data_siswa, start=1):
    print(f"{idx}.   {siswa['Nama']}\t{siswa['NIM']}\t\t{siswa['Tugas']}\t{siswa['UTS']}\t{siswa['UAS']}\t{siswa['Nilai Akhir']}")
