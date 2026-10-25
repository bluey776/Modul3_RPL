from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

if daftar_buku:
    # Ambil ID buku terakhir yang baru ditambahkan untuk diuji Update dan Delete
    target_id = daftar_buku[-1]['id_buku']

    # 3. Menguji fungsi Update
    print(f"\n3. Mengubah data buku dengan ID {target_id}...")
    model.update_buku(target_id, "Python MVC Edisi Revisi", "Guido van Rossum", 2024)
    print("Data buku berhasil diperbarui!")

    print("\n=== Daftar Buku (Setelah Update) ===")
    for buku in model.get_all_buku():
        print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

    # 4. Menguji fungsi Delete
    print(f"\n4. Menghapus data buku dengan ID {target_id}...")
    model.delete_buku(target_id)
    print("Data buku berhasil dihapus!")

    print("\n=== Daftar Buku (Setelah Delete) ===")
    daftar_akhir = model.get_all_buku()
    if daftar_akhir:
        for buku in daftar_akhir:
            print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")
    else:
        print("(Tabel buku kosong)")