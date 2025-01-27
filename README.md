# Currency Converter CLI

## Deskripsi
Program ini adalah alat konversi mata uang sederhana yang memungkinkan pengguna untuk mengonversi jumlah uang dari satu mata uang ke mata uang lain. Program ini mengambil nilai tukar terkini menggunakan API dari [ExchangeRate-API](https://www.exchangerate-api.com/) dan menghitung konversi berdasarkan nilai tukar yang didapatkan.

## Fitur
- Mengonversi jumlah uang dari satu mata uang ke mata uang lainnya.
- Menyediakan hasil konversi berdasarkan nilai tukar terkini.
- Memungkinkan pengguna untuk memilih mata uang asal dan tujuan.

## Prasyarat
- Python 3.x
- Pustaka `requests` untuk melakukan permintaan HTTP ke API.
  - Install pustaka `requests` jika belum terpasang:
    ```bash
    pip install requests
    ```

## Instalasi

1. Pastikan Python sudah terpasang di sistem Anda.
2. Install pustaka `requests` untuk melakukan HTTP request:
    ```bash
    pip install requests
    ```

3. Unduh atau salin kode program `currency_converter.py` ke dalam direktori proyek Anda.

## Penggunaan

1. **Jalankan Program**:
    Setelah menginstal `requests`, jalankan program menggunakan Python di terminal atau command prompt:
    ```bash
    python currency_converter.py
    ```

2. **Masukkan Input**:
    Program akan meminta Anda untuk memasukkan:
    - **Jumlah uang yang ingin dikonversi**.
    - **Mata uang asal** (contoh: USD untuk Dolar Amerika).
    - **Mata uang tujuan** (contoh: EUR untuk Euro).

3. **Lihat Hasil**:
    Setelah Anda memasukkan data, program akan mengambil nilai tukar terkini dan menghitung konversi dari mata uang asal ke mata uang tujuan, lalu menampilkan hasilnya di terminal.

### Contoh Penggunaan:
```bash
Masukkan jumlah uang yang ingin dikonversi:
1
Masukkan mata uang asal (contoh: USD):
USD
Masukkan mata uang tujuan (contoh: EUR):
IDR
```

**Output:**
```bash
1.0 USD = 16179.70 IDR
```

Jika ada kesalahan (misalnya, mata uang tujuan tidak valid), maka program akan menampilkan pesan kesalahan seperti:
```bash
Tidak ada data nilai tukar untuk XYZ.
```

## Penjelasan Kode

### `convert_currency(amount, from_currency, to_currency)`
- **Deskripsi**: Fungsi ini mengonversi jumlah uang (`amount`) dari mata uang asal (`from_currency`) ke mata uang tujuan (`to_currency`).
- **Langkah-langkah**:
  1. Mengambil data nilai tukar terkini dari API `exchangerate-api.com` menggunakan `requests.get()`.
  2. Memeriksa apakah data nilai tukar berhasil diambil (ada dalam `data['rates']`).
  3. Jika ada nilai tukar untuk mata uang tujuan (`to_currency`), konversi jumlah uang dengan mengalikan jumlah dengan nilai tukar yang ditemukan.
  4. Menampilkan hasil konversi.
  5. Jika mata uang tujuan tidak ada dalam data nilai tukar, menampilkan pesan kesalahan.
  6. Jika terjadi masalah dengan permintaan API, menampilkan pesan kegagalan.

### `main()`
- **Deskripsi**: Fungsi utama yang menjalankan program, meminta input dari pengguna untuk jumlah uang, mata uang asal, dan mata uang tujuan, kemudian memanggil fungsi `convert_currency()` untuk melakukan konversi dan menampilkan hasilnya.

## Catatan:
- Program ini menggunakan layanan API eksternal **ExchangeRate-API**, yang memiliki batasan jumlah permintaan gratis per hari. Jika jumlah permintaan melebihi batas yang diberikan oleh layanan API, maka aplikasi akan gagal mendapatkan data nilai tukar dan menampilkan pesan kesalahan.
- Pastikan untuk menggunakan kode mata uang yang benar sesuai dengan standar internasional (misalnya, USD, EUR, IDR, dll).
