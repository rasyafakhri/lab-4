# lab-4
## Tentu, berikut adalah penjelasan mengenai penguraian kode yang telah disediakan: 1.Fungsi "hitung_nilai`:
   ## - Fungsi ini digunakan untuk menghitung nilai akhir dari seorang siswa berdasarkan komponen nilai yang telah ditentukan (tugas: 30%, UTS: 35%, UAS: 35%).
   ## - Fungsi ini menerima tiga parameter yaitu `tugas`, `uts`, dan `uas` yang merupakan nilai dari tugas, UTS, dan UAS siswa.
   ## - Menggunakan rumus `(0.3 * tugas) + (0.35 * uts) + (0.35 * uas)` untuk menghitung nilai akhir.

## 2. Inisialisasi List `data_siswa`:
   ## - Sebuah list kosong dibuat untuk menyimpan data siswa, setiap data siswa akan disimpan dalam bentuk dictionary.

## 3. Perulangan dengan `while True`:
   ## - Program menggunakan perulangan tak terbatas `while True` untuk meminta pengguna memasukkan data siswa secara berulang.

## 4. Input Data Siswa**:
   ## - Pengguna diminta untuk memasukkan NIM, nama, nilai tugas, UTS, dan UAS siswa secara berurutan menggunakan fungsi `input`.
   ## - Nilai-nilai yang dimasukkan oleh pengguna akan disimpan dalam variabel `nim`, `nama`, `tugas`, `uts`, dan `uas`.

## 5. penghitungan Nilai Akhir:
## - Setelah semua nilai dimasukkan, program memanggil fungsi `hitung_nilai` dengan nilai-nilai tugas, UTS, dan UAS yang telah dimasukkan sebagai parameter.
  ## - Nilai akhir kemudian dihitung menggunakan rumus yang telah ditentukan.

## 6. Penyimpanan Data:
   ## - Data siswa beserta nilai akhirnya disimpan dalam bentuk dictionary yang memiliki kunci (key) berupa `NIM`, `Nama`, `Tugas`, `UTS`, `UAS`, dan `Nilai Akhir`.
   ## - Dictionary ini kemudian ditambahkan ke dalam list `data_siswa` menggunakan method `.append()`.

## 7. Pertanyaan untuk Menambah Data Lagi:
   ## - Setelah data siswa dimasukkan, program akan bertanya apakah pengguna ingin menambahkan data siswa lagi atau tidak.
   ## - Jika pengguna memilih untuk tidak menambahkan data lagi (`tambah_data.lower() != 'y'`), perulangan `while` akan berakhir.

## 8. Menampilkan Daftar Data Siswa:
   ## - Program akan mencetak daftar data siswa yang telah dimasukkan.
   ## - Menggunakan perulangan `for` untuk menampilkan setiap elemen dari list `data_siswa`.
   ## - Data siswa ditampilkan berupa tabel dengan NIM, nama, nilai tugas, UTS, UAS, dan nilai akhir yang dihitung sebelumnya.