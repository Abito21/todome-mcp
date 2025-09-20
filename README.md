# todome-mcp

Todome-MCP adalah sebuah modul/skrip Python sederhana untuk mengelola **Multiple Choice Problems (MCP)** dalam aplikasi manajemen tugas (“todo”). Tujuannya adalah meningkatkan fleksibilitas dalam memberi soal pilihan ganda serta integrasinya ke dalam sistem todo.

---

## ✨ Fitur

- CRUD soal pilihan ganda: membuat, membaca, memperbarui, menghapus soal.  
- Penyimpanan sederhana menggunakan file database SQLite (`todos.db`) agar ringan dan mudah dijalankan.  
- Struktur koding modular: terdapat `basic_mcp.py` & `todos_mcp.py` yang masing-masing memiliki tanggung jawab spesifik.  
- Konfigurasi via `pyproject.toml` untuk dependensi dan pengaturan proyek Python.  

---

## ⚙️ Instalasi

1. Clone repositori:

   ```bash
   git clone https://github.com/Abito21/todome-mcp.git
   cd todome-mcp
   ```

2. Siapkan virtual environment (opsional, tapi disarankan):

   ```bash
    python -m venv venv
    source venv/bin/activate   # pada Linux/macOS
    venv\Scripts\activate      # pada Windows
   ```

3. Install dependensi:

   ```bash
   uv install -r requirements.txt
   ```

(Jika belum ada file requirements.txt, bisa dibuat dari isi pyproject.toml.)

---

## 🚀 Penggunaan

Berikut contoh langkah-penggunaan dasar:

basic_mcp.py — modul inti untuk operasi Multiple Choice.

todos_mcp.py — modul yang mengintegrasikan MCP ke dalam alur manajemen tugas.

Contoh:

```bash
python todos_mcp.py
```

Kemudian ikuti instruksi di terminal (jika ada) untuk menambahkan soal, melihat daftar, dsb.

---

## 📂 Struktur Proyek

```
todome-mcp/
├── app/             # (jika ada) modul utama aplikasi
├── basic_mcp.py     # logika dasar MCP
├── todos_mcp.py     # integrasi ke sistem todo
├── todos.db         # database SQLite
├── pyproject.toml   # konfigurasi proyek
├── .gitignore
└── README.md
```

---