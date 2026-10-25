from models.anggota_model import AnggotaModel

model_anggota = AnggotaModel()

# 1. Menguji fungsi Create (menambah anggota baru)
print("Menambahkan data anggota...")
model_anggota.create_anggota("Budi Santoso", "Jl. Merdeka No. 45")
model_anggota.create_anggota("Siti Rahma", "Jl. Diponegoro No. 12")
print("Data anggota berhasil disimpan ke database!")

# 2. Menguji fungsi Read (menampilkan seluruh data anggota)
print("\n=== Daftar Anggota Perpustakaan ===")
daftar_anggota = model_anggota.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - Alamat: {anggota['alamat']}")