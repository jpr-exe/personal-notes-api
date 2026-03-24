# API Pencatatan Personal

API sederhana untuk mengelola catatan pribadi, dibangun dengan Python + Flask.

## Teknologi yang Digunakan
- Python 3.11
- Flask 3.0.0
- Docker
- GitHub Actions

## Cara Menjalankan

### Tanpa Docker
```bash
pip install -r requirements.txt
python app.py
```

### Dengan Docker
```bash
docker-compose up
```

## Endpoint API

| Method | Endpoint | Kegunaan |
|--------|----------|----------|
| GET | /catatan | Ambil semua catatan |
| POST | /catatan | Buat catatan baru |
| GET | /catatan/{id} | Ambil satu catatan |
| PUT | /catatan/{id} | Edit catatan |
| DELETE | /catatan/{id} | Hapus catatan |

## Contoh Request

### Buat Catatan Baru
```json
POST /catatan
{
    "judul": "Catatan Pertama",
    "isi": "Ini isi catatan saya"
}
```

### Contoh Response Sukses
```json
{
    "status": "OK",
    "pesan": "Catatan berhasil dibuat",
    "data": {
        "id": 1,
        "judul": "Catatan Pertama",
        "isi": "Ini isi catatan saya"
    },
    "kesalahan": null
}
```

## Menjalankan Unit Test
```bash
pytest tests/
```