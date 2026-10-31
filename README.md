# Aplikasi Perpustakaan

Aplikasi desktop manajemen perpustakaan berbasis Python dengan antarmuka
CustomTkinter dan database MySQL, dibangun dengan arsitektur MVC
(Model-View-Controller).

Fitur utama:

- Login dengan password ter-hash SHA-256
- Manajemen data buku dan anggota (tambah, perbarui, hapus)
- Otorisasi berbasis role: **admin** (akses penuh) dan **anggota** (hanya melihat data)
- Logout kembali ke halaman login
- CI/CD dengan GitHub Actions (flake8 dan pytest)

## Struktur Direktori

```
modul 3/
├── .github/workflows/
│   └── ci_pipeline.yml        # Pipeline CI (flake8 + pytest)
├── config/
│   └── database.py            # Konfigurasi koneksi MySQL
├── models/                    # Model: akses data ke database
├── views/                     # View: tampilan antarmuka (CustomTkinter)
├── controllers/
│   ├── auth_controller.py     # Logika login
│   ├── buku_controller.py     # Logika data buku + otorisasi
│   └── anggota_controller.py  # Logika data anggota
├── tests/                     # Unit test (pytest)
├── main.py                    # Titik masuk aplikasi
├── main_buku.py
├── main_anggota.py
├── requirements.txt
└── README.md
```

## Instalasi dan Konfigurasi Database

### 1. Prasyarat
- Python 3.11 atau lebih baru
- MySQL Server (contoh: Laragon) dan HeidiSQL

### 2. Clone repositori dan install dependensi
```bash
git clone https://github.com/bluey776/Modul3_RPL.git
cd Modul3_RPL
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### 3. Buat database dan tabel
Jalankan SQL berikut di HeidiSQL:

```sql
CREATE DATABASE perpustakaan;
USE perpustakaan;

CREATE TABLE buku (
    id_buku INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(150) NOT NULL,
    penulis VARCHAR(100) NOT NULL,
    tahun_terbit INT NOT NULL
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(64) NOT NULL,
    role ENUM('admin', 'anggota') NOT NULL
);
```

Tabel anggota dibuat sesuai struktur yang dipakai `anggota_controller.py`.

### 4. Konfigurasi koneksi
Buka `config/database.py`, lalu sesuaikan `host`, `db_name`, `username`,
dan `password` dengan MySQL di komputer Anda. Bawaan: `localhost`,
`perpustakaan`, `root`, password kosong.

### 5. Buat akun awal
Password disimpan sebagai hash SHA-256 lewat `register_user()`:

```python
from models.user_model import UserModel
um = UserModel()
um.register_user("admin", "admin123", "admin")
um.register_user("mahasiswa", "user123", "anggota")
```

## Cara Menjalankan Aplikasi

Pastikan MySQL sudah berjalan, lalu:

```bash
python main.py
```

Login sebagai `admin` untuk akses penuh, atau `mahasiswa` untuk mode anggota
(tombol aksi dikunci).

Menjalankan pengujian:
```bash
pytest -v
```

Versi siap pakai (`AplikasiPerpustakaan.exe`) tersedia di halaman
**Releases** repositori ini. MySQL tetap harus aktif saat menjalankannya.