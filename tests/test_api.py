import pytest
from app import app

@pytest.fixture
def klien():
    app.config["TESTING"] = True
    with app.test_client() as klien:
        yield klien

def test_ambil_semua_catatan_kosong(klien):
    hasil = klien.get("/catatan")
    assert hasil.status_code == 200
    assert hasil.get_json()["status"] == "OK"

def test_buat_catatan_berhasil(klien):
    hasil = klien.post("/catatan", json={
        "judul": "Belajar Docker",
        "isi": "Docker adalah platform containerization"
    })
    assert hasil.status_code == 201
    assert hasil.get_json()["data"]["judul"] == "Belajar Docker"

def test_buat_catatan_tanpa_judul(klien):
    hasil = klien.post("/catatan", json={"isi": "isi catatan"})
    assert hasil.status_code == 400
    assert hasil.get_json()["status"] == "ERROR"

def test_hapus_catatan_tidak_ada(klien):
    hasil = klien.delete("/catatan/999")
    assert hasil.status_code == 404
    assert hasil.get_json()["status"] == "ERROR"