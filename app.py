from flask import Flask, jsonify, request

app = Flask(__name__)

daftar_catatan = []
id_berikutnya = 1

def buat_response(status, pesan, data=None, kesalahan=None):
    return jsonify({
        "status": status,
        "pesan": pesan,
        "data": data,
        "kesalahan": kesalahan
    })

@app.route("/catatan", methods=["GET"])
def ambil_semua_catatan():
    return buat_response("OK", "Catatan berhasil diambil", daftar_catatan), 200

@app.route("/catatan/<int:id_catatan>", methods=["GET"])
def ambil_satu_catatan(id_catatan):
    catatan = next((c for c in daftar_catatan if c["id"] == id_catatan), None)
    if not catatan:
        return buat_response("ERROR", "Catatan tidak ditemukan", kesalahan=["Catatan tidak ditemukan"]), 404
    return buat_response("OK", "Catatan berhasil diambil", catatan), 200

@app.route("/catatan", methods=["POST"])
def buat_catatan():
    global id_berikutnya
    isi_request = request.get_json()

    if not isi_request or not isi_request.get("judul"):
        return buat_response("ERROR", "Validasi gagal", kesalahan=["judul wajib diisi"]), 400
    if not isi_request.get("isi"):
        return buat_response("ERROR", "Validasi gagal", kesalahan=["isi wajib diisi"]), 400

    catatan_baru = {
        "id": id_berikutnya,
        "judul": isi_request["judul"],
        "isi": isi_request["isi"]
    }
    daftar_catatan.append(catatan_baru)
    id_berikutnya += 1
    return buat_response("OK", "Catatan berhasil dibuat", catatan_baru), 201

@app.route("/catatan/<int:id_catatan>", methods=["PUT"])
def ubah_catatan(id_catatan):
    catatan = next((c for c in daftar_catatan if c["id"] == id_catatan), None)
    if not catatan:
        return buat_response("ERROR", "Catatan tidak ditemukan", kesalahan=["Catatan tidak ditemukan"]), 404

    isi_request = request.get_json()
    if not isi_request or not isi_request.get("judul"):
        return buat_response("ERROR", "Validasi gagal", kesalahan=["judul wajib diisi"]), 400
    if not isi_request.get("isi"):
        return buat_response("ERROR", "Validasi gagal", kesalahan=["isi wajib diisi"]), 400

    catatan["judul"] = isi_request["judul"]
    catatan["isi"] = isi_request["isi"]
    return buat_response("OK", "Catatan berhasil diubah", catatan), 200

@app.route("/catatan/<int:id_catatan>", methods=["DELETE"])
def hapus_catatan(id_catatan):
    global daftar_catatan
    catatan = next((c for c in daftar_catatan if c["id"] == id_catatan), None)
    if not catatan:
        return buat_response("ERROR", "Catatan tidak ditemukan", kesalahan=["Catatan tidak ditemukan"]), 404

    daftar_catatan = [c for c in daftar_catatan if c["id"] != id_catatan]
    return buat_response("OK", "Catatan berhasil dihapus"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)