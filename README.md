# Sistem Digital Signature Menggunakan Algoritma RSA & SHA-256

Proyek ini merupakan implementasi sistem pengamanan dokumen digital menggunakan skema **Digital Signature**. Sistem ini mengintegrasikan fungsi Hashing (SHA-256) untuk menjaga integritas dokumen dan Algoritma Asimetris (RSA) untuk autentikasi serta aspek *non-repudiation* (anti-penyangkalan).

---

## 👥 Anggota Tim & Pembagian Tugas

Proyek ini diselesaikan secara kolaboratif oleh tim yang terbagi menjadi dua fokus utama:

### 🛠️ Tim Sistem
* **Orang 1 – Backend Developer (Python):** 
  * Implementasi matematika algoritma RSA (Key Generation, Enkripsi, Dekripsi).
  * Pembuatan modul enkripsi hash dokumen menggunakan SHA-256.
  * Penyusunan logika *Digital Signing* dan *Verification*.
* **Orang 2 – Frontend Developer (Interface):**
  * Perancangan Graphical User Interface (GUI).
  * Implementasi fitur upload file PDF/TXT.
  * Integrasi antarmuka dengan fungsionalitas backend.

### 📝 Tim Laporan
* **Orang 3 – Penyusun BAB I (Pendahuluan):** Latar belakang, identifikasi & rumusan masalah, tujuan, dan manfaat penelitian.
* **Orang 4 – Penyusun BAB II (Tinjauan Pustaka):** Teori Digital Signature, Kriptografi RSA, SHA-256, dan analisis penelitian terdahulu.
* **Orang 5 – Penyusun BAB III (Metodologi):** Use Case Diagram, Activity Diagram, Flowchart, dan desain arsitektur sistem.
* **Orang 6 – Penyusun BAB IV & V (Hasil & Kesimpulan):** Dokumentasi pengujian sistem (valid & tidak valid), analisis hasil, kesimpulan, serta saran pengembangan.

---

## 🏗️ Struktur Folder Repository

```text
├── backend/                  # Folder Utama Aplikasi (Gabungan Sistem)
│   ├── __pycache__/          # File cache otomatis Python (abaikan/masuk .gitignore)
│   ├── rsa_core.py           # Logika Inti Algoritma RSA (Keygen, Sign, Verify) - Tugas Orang 1
│   ├── utils.py              # Utilitas Hashing Dokumen (SHA-256) - Tugas Orang 1
│   └── app.py                # Interface GUI PyQt (Frontend) - Tugas Orang 2
│
├── .gitignore                # Pengecualian file sampah Git (seperti __pycache__)
└── README.md                 # Dokumentasi Utama Proyek
