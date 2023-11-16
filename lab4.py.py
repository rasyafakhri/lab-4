# Fungsi untuk menghitung nilai akhir berdasarkan komponen nilai
def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)
    return nilai_akhir

# Inisialisasi list untuk menyimpan data
data_siswa = []

# Perulangan untuk memasukkan data
while True:
    nama = input("Masukkan Nama siswa: ")
    nim = input("Masukkan NIM siswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    # Memanggil fungsi hitung_nilai untuk menghitung nilai akhir
    nilai_akhir = hitung_nilai(tugas, uts, uas)

    # Menambahkan data ke dalam list
    data_siswa.append({
        'Nama': nama,
        'NIM': nim,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    })

    # Tanya apakah ingin menambah data lagi atau tidak
    tambah_data = input("Tambah data lagi? (y/t): ")
    if tambah_data.lower() != 'y':
        break

# Menampilkan daftar data
print("\nDaftar Data Siswa:")
print("===================================================================")
print("No.  Nama\tNIM\t\tTugas\tUTS\tUAS\tNilai Akhir")
print("===================================================================")
for idx, siswa in enumerate(data_siswa, start=1):
    print(f"{idx}.   {siswa['Nama']}\t{siswa['NIM']}\t\t{siswa['Tugas']}\t{siswa['UTS']}\t{siswa['UAS']}\t{siswa['Nilai Akhir']}")
