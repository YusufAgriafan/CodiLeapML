# Flask Summarization API

API ini digunakan untuk menghasilkan ringkasan teks menggunakan model *machine learning* berbasis **T5**. Anda dapat membersihkan teks dari tag HTML dan mendapatkan ringkasan dalam format JSON.

## Prasyarat

1. **Python** versi 3.8 atau lebih baru.
2. Pastikan Anda sudah menginstal **pip**.
3. Model dan tokenizer tersedia di direktori lokal `./CodiLeapML/summarization`.

## Instalasi

1. **Clone repository** ini atau salin kode.
2. Pastikan Anda berada di direktori proyek.
3. Instal dependensi:

   ```
   pip install -r requirements.txt
   ```

## Prasyarat

1. Jalankan `app.py`:

   ```
   python app.py
   ```
2. Aplikasi akan berjalan pada `http://127.0.0.1:5000` secara default.

## Menguji Endpoint Menggunakan Postman

1. **Buka Postman** dan buat request baru:

   - Pilih metode: `POST`.
   - Masukkan URL: `http://127.0.0.1:5000/summarize`.
2. **Tambahkan Body ke Request**:

   - Pilih tab `Body`.
   - Pilih `raw`.
   - Atur format menjadi `JSON`.
   - Masukkan data berikut di bagian *raw body*:
     ```json
     {
       "text": "<p>Ini adalah contoh teks dengan <b>HTML</b> yang akan diringkas.</p>"
     }
     ```
3. **Kirim Request**:

   - Klik tombol **Send**.
   - Anda akan menerima respons berupa ringkasan dalam format JSON, misalnya:
     ```json
     {
       "summary": "Ini adalah contoh teks yang akan diringkas."
     }
     ```
