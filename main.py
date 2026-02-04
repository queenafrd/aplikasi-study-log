catatan = []
target_harian = None  # dalam menit, None jika belum diatur

def tambah_catatan():
    mapel = input("Mapel: ").strip()
    topik = input("Topik: ").strip()
    durasi_str = input("Durasi belajar (menit): ").strip()

    if not mapel or not topik or not durasi_str:
        print("Semua field harus diisi.")
        return

    try:
        durasi = int(durasi_str)
        if durasi <= 0:
            print("Durasi harus berupa angka positif.")
            return
    except ValueError:
        print("Durasi harus berupa angka (menit).")
        return

    entry = {"mapel": mapel, "topik": topik, "durasi": durasi}
    catatan.append(entry)
    print("Catatan berhasil ditambahkan.")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan.")
        return

    # Hitung lebar kolom untuk penjajaran
    idx_w = len(str(len(catatan)))
    mapel_w = max(len("Mapel"), *(len(c["mapel"]) for c in catatan))
    topik_w = max(len("Topik"), *(len(c["topik"]) for c in catatan))
    durasi_w = max(len("Durasi"), *(len(str(c["durasi"])) for c in catatan))

    print("\nDaftar catatan:")
    header = f"{'No'.ljust(idx_w)}  {'Mapel'.ljust(mapel_w)}  {'Topik'.ljust(topik_w)}  {'Durasi'.rjust(durasi_w)}"
    sep = f"{'-'*idx_w}  {'-'*mapel_w}  {'-'*topik_w}  {'-'*durasi_w}"
    print(header)
    print(sep)

    for i, c in enumerate(catatan, 1):
        no = str(i).ljust(idx_w)
        m = c["mapel"].ljust(mapel_w)
        t = c["topik"].ljust(topik_w)
        d = str(c["durasi"]).rjust(durasi_w)
        print(f"{no}  {m}  {t}  {d} menit")

def total_waktu():
    if not catatan:
        print("Belum ada catatan.")
        return
    total = sum(c['durasi'] for c in catatan)
    jam = total // 60
    menit = total % 60
    if jam:
        print(f"Total waktu belajar: {jam} jam {menit} menit ({total} menit)")
    else:
        print(f"Total waktu belajar: {menit} menit")

    # Jika target harian diatur, tampilkan status terhadap target
    if target_harian is not None:
        if total >= target_harian:
            lebih = total - target_harian
            if lebih:
                print(f"Target harian tercapai — berlebih {lebih} menit.")
            else:
                print("Target harian tercapai tepat.")
        else:
            sisa = target_harian - total
            print(f"Belum mencapai target harian. Sisa {sisa} menit.")


def atur_target_harian():
    """Menampilkan target saat ini lalu meminta input target dalam menit."""
    global target_harian
    if target_harian is not None:
        jam = target_harian // 60
        menit = target_harian % 60
        if jam:
            print(f"Target saat ini: {jam} jam {menit} menit ({target_harian} menit)")
        else:
            print(f"Target saat ini: {menit} menit")
    else:
        print("Belum ada target harian.")

    nilai = input("Masukkan target harian (menit) atau kosongkan untuk batal: ").strip()
    if nilai == "":
        print("Batal mengatur target.")
        return

    try:
        t = int(nilai)
        if t <= 0:
            print("Target harus berupa angka positif.")
            return
    except ValueError:
        print("Input tidak valid — masukkan angka (menit).")
        return

    target_harian = t
    print(f"Target harian disimpan: {target_harian} menit.")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Atur target harian")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    elif pilihan == "5":
        atur_target_harian()
    else:
        print("Pilihan tidak valid")