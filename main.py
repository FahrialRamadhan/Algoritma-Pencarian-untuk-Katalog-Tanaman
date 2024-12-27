import time

katalog_tanaman = [
"Jambu", "Mawar", "Kaktus", "Anggrek", "Pandan", "Melati", "Durian", "Bambu", 
  "Pinus", "Lidah Buaya", "Anggur", "Blueberry", "Kacang Hijau", "Kacang Merah", 
  "Padi", "Jagung", "Gandum", "Kentang", "Labu", "Zucchini", "Pohon Kurma", 
  "Pohon Karet", "Bayam", "Kale", "Daun Bawang", "Petai", "Jengkol", "Labu Air", 
  "Singkong", "Sawi", "Kembang Kol", "Bawang Putih", "Bawang Merah", "Cabai", 
  "Lengkuas Merah", "Sereh Wangi", "Pandan Wangi", "Tebu", "Buncis", "Terung", 
  "Mentimun", "Belimbing Wuluh", "Durian Montong", "Mangga Harum Manis", 
  "Jeruk Nipis", "Pepaya", "Nanas", "Melon", "Semangka Kuning", "Markisa Manis", 
  "Salak Pondoh", "Rambutan Rapiah", "Pohon Jati", "Mahoni", "Kapur", "Pinang", 
  "Kemuning", "Kenari", "Pohon Aren", "Pohon Kelapa", "Pala", "Cengkeh", "Kayu Manis", 
  "Vanili", "Kakao", "Kopi", "Asam Jawa", "Ketumbar", "Jahe", "Kunyit", "Temulawak", 
  "Kapulaga", "Serai", "Daun Kemangi", "Daun Jeruk", "Daun Salam", "Pohon Mangga", 
  "Pohon Alpukat", "Pohon Durian", "Pohon Apel", "Pohon Jeruk", "Pohon Pisang", 
  "Pohon Nangka", "Pohon Sukun", "Pohon Delima", "Pohon Kersen", "Pohon Sawo", 
  "Pohon Cempedak", "Pohon Rambutan", "Pohon Jambu Air", "Pohon Jambu Biji", 
  "Pohon Kedondong", "Pohon Keluwih", "Pohon Bidara", "Pohon Matoa", "Pohon Duku", 
  "Pohon Langsat", "Pohon Srikaya", "Pohon Belimbing", "Pohon Leci", "Pohon Mangosteen", 
  "Pohon Pisang Raja", "Pohon Pisang Ambon", "Pohon Aren", "Pohon Kurma", "Pohon Kelapa Sawit", 
  "Pohon Sengon", "Pohon Waru", "Pohon Beringin", "Pohon Akasia", "Pohon Eukaliptus", 
  "Pohon Cemara"
]

karakteristik_tanaman = [
    "Memiliki karakteristik buah manis dan berair, kulit halus, dan sering dikonsumsi segar",  # Jambu
    "Memiliki karakteristik bunga berduri dengan warna-warna cerah dan aroma harum",  # Mawar
    "Memiliki karakteristik batang berduri dengan berbagai bentuk, tahan di lingkungan kering",  # Kaktus
    "Memiliki karakteristik bunga eksotis yang indah, sering digunakan sebagai tanaman hias",  # Anggrek
    "Memiliki karakteristik daun wangi yang sering digunakan untuk masakan atau pewangi",  # Pandan
    "Memiliki karakteristik bunga putih harum, melambangkan kesucian",  # Melati
    "Memiliki karakteristik buah besar berduri dengan aroma kuat, daging manis",  # Durian
    "Memiliki karakteristik batang beruas-ruas yang kuat, sering digunakan untuk bahan bangunan",  # Bambu
    "Memiliki karakteristik pohon tinggi dengan daun jarum, sering digunakan sebagai dekorasi",  # Pinus
    "Memiliki karakteristik daun berdaging dengan gel yang sering digunakan untuk obat atau kosmetik",  # Lidah Buaya
    "Memiliki karakteristik buah kecil berwarna ungu, tumbuh merambat",  # Anggur
    "Memiliki karakteristik buah kecil berwarna biru, sering digunakan untuk jus atau makanan penutup",  # Blueberry
    "Memiliki karakteristik tanaman pendek dengan biji hijau yang kaya protein",  # Kacang Hijau
    "Memiliki karakteristik tanaman pendek dengan biji merah, kaya nutrisi",  # Kacang Merah
    "Memiliki karakteristik tanaman dengan biji kecil sebagai bahan makanan pokok",  # Padi
    "Memiliki karakteristik tanaman tinggi dengan biji kuning, digunakan sebagai makanan dan bahan baku industri",  # Jagung
    "Memiliki karakteristik tanaman dengan biji kecil yang digunakan untuk tepung atau roti",  # Gandum
    "Memiliki karakteristik tanaman umbi besar yang kaya karbohidrat",  # Kentang
    "Memiliki karakteristik tanaman merambat dengan buah besar, kulit keras, dan daging oranye",  # Labu
    "Memiliki karakteristik tanaman dengan buah lonjong, kulit hijau, dan daging putih",  # Zucchini
    "Memiliki karakteristik pohon dengan buah manis yang kaya energi, sering dijadikan kurma kering",  # Pohon Kurma
    "Memiliki karakteristik pohon tinggi dengan getah yang digunakan untuk bahan baku karet",  # Pohon Karet
    "Memiliki karakteristik daun hijau yang kaya nutrisi, sering digunakan dalam masakan",  # Bayam
    "Memiliki karakteristik daun hijau keriting, kaya akan vitamin dan mineral",  # Kale
    "Memiliki karakteristik daun panjang berwarna hijau, sering digunakan sebagai bumbu masakan",  # Daun Bawang
    "Memiliki karakteristik buah panjang dengan aroma kuat, sering dikonsumsi sebagai lalapan",  # Petai
    "Memiliki karakteristik buah dengan aroma khas, sering digunakan dalam masakan tradisional",  # Jengkol
    "Memiliki karakteristik buah kecil berkulit hijau muda, sering digunakan dalam sayur",  # Labu Air
    "Memiliki karakteristik tanaman umbi besar dengan kulit cokelat dan daging putih",  # Singkong
    "Memiliki karakteristik daun hijau yang sering digunakan untuk tumis atau sup",  # Sawi
    "Memiliki karakteristik bunga hijau besar yang dapat dimakan, kaya nutrisi",  # Kembang Kol
    "Memiliki karakteristik umbi putih kecil dengan aroma kuat, sering digunakan sebagai bumbu",  # Bawang Putih
    "Memiliki karakteristik umbi merah kecil dengan aroma tajam, digunakan dalam berbagai masakan",  # Bawang Merah
    "Memiliki karakteristik buah kecil berwarna merah atau hijau, rasanya pedas",  # Cabai
    "Memiliki karakteristik rimpang berwarna merah muda, sering digunakan sebagai bumbu dapur",  # Lengkuas Merah
    "Memiliki karakteristik tanaman tinggi dengan aroma wangi, digunakan untuk minuman dan masakan",  # Sereh Wangi
    "Memiliki karakteristik daun panjang beraroma khas, digunakan untuk masakan dan pewangi",  # Pandan Wangi
    "Memiliki karakteristik tanaman tinggi dengan batang yang menghasilkan gula",  # Tebu
    "Memiliki karakteristik tanaman kecil dengan buah hijau panjang, kaya serat",  # Buncis
    "Memiliki karakteristik tanaman dengan buah ungu atau hijau berbentuk lonjong",  # Terung
    "Memiliki karakteristik buah hijau kecil berair, sering digunakan sebagai acar",  # Mentimun
    "Memiliki karakteristik buah hijau kecil dengan rasa asam, digunakan dalam masakan",  # Belimbing Wuluh
    "Memiliki karakteristik buah berduri besar dengan aroma kuat dan rasa manis",  # Durian Montong
    "Memiliki karakteristik buah besar berwarna kuning, manis, dan harum",  # Mangga Harum Manis
    "Memiliki karakteristik buah kecil berwarna hijau, kaya vitamin C, sering digunakan sebagai bahan minuman",  # Jeruk Nipis
    "Memiliki karakteristik buah tropis besar berwarna oranye dengan daging manis",  # Pepaya
    "Memiliki karakteristik buah besar berwarna kuning dengan aroma segar dan daging manis",  # Nanas
    "Memiliki karakteristik buah bulat besar dengan kulit keras dan daging manis",  # Melon
    "Memiliki karakteristik buah bulat besar berwarna kuning dengan daging berair",  # Semangka Kuning
    "Memiliki karakteristik buah bulat kecil dengan rasa manis dan asam",  # Markisa Manis
    "Memiliki karakteristik buah kecil bersisik dengan rasa manis dan asam",  # Salak Pondoh
    "Memiliki karakteristik buah kecil berbulu dengan rasa manis dan segar",  # Rambutan Rapiah
    "Memiliki karakteristik pohon besar dengan kayu kuat, sering digunakan untuk bahan bangunan",  # Pohon Jati
    "Memiliki karakteristik pohon besar dengan kayu keras yang tahan lama",  # Mahoni
    "Memiliki karakteristik pohon dengan kayu wangi, sering digunakan sebagai bahan baku mebel",  # Kapur
    "Memiliki karakteristik pohon tinggi dengan buah berbentuk lonjong",  # Pinang
    "Memiliki karakteristik pohon kecil dengan bunga beraroma wangi, sering digunakan untuk bahan obat",  # Kemuning
    "Memiliki karakteristik pohon dengan buah kecil berbentuk lonjong, kaya akan minyak",  # Kenari
    "Memiliki karakteristik pohon tinggi dengan batang penghasil gula aren",  # Pohon Aren
    "Memiliki karakteristik pohon tinggi dengan buah bulat berair, digunakan untuk berbagai produk makanan",  # Pohon Kelapa
    "Memiliki karakteristik pohon dengan buah berbentuk bulat kecil, kaya rempah",  # Pala
    "Memiliki karakteristik pohon dengan bunga kecil berbentuk lonjong, kaya rempah",  # Cengkeh
    "Memiliki karakteristik pohon dengan kulit batang wangi, digunakan untuk rempah",  # Kayu Manis
    "Memiliki karakteristik tanaman merambat dengan buah berbentuk panjang, digunakan untuk bahan baku vanili",  # Vanili
    "Memiliki karakteristik pohon penghasil biji cokelat yang dapat diolah menjadi bubuk kokoa dan cokelat, dengan buah berukuran sedang berbentuk lonjong yang berisi biji-biji yang diselimuti pulp putih",  # Kakao
    "Memiliki karakteristik pohon penghasil biji untuk minuman kopi, dengan aroma khas",  # Kopi
    "Memiliki karakteristik pohon dengan buah berbentuk lonjong dan rasa asam, digunakan untuk bumbu",  # Asam Jawa
    "Memiliki karakteristik tanaman pendek dengan biji kecil beraroma khas, digunakan sebagai bumbu",  # Ketumbar
    "Memiliki karakteristik tanaman rimpang berwarna kuning, sering digunakan sebagai bahan obat dan masakan",  # Jahe
    "Memiliki karakteristik rimpang kuning cerah dengan aroma khas, digunakan untuk rempah",  # Kunyit
    "Memiliki karakteristik rimpang besar dengan aroma khas, digunakan dalam masakan dan obat",  # Temulawak
    "Memiliki karakteristik buah kecil beraroma khas, sering digunakan untuk minuman atau masakan",  # Kapulaga
    "Memiliki karakteristik batang beraroma khas, sering digunakan untuk masakan",  # Serai
    "Memiliki karakteristik daun hijau kecil beraroma wangi, digunakan dalam masakan",  # Daun Kemangi
    "Memiliki karakteristik daun hijau beraroma segar, sering digunakan sebagai bumbu masakan",  # Daun Jeruk
    "Memiliki karakteristik daun hijau dengan aroma khas, digunakan dalam masakan tradisional",  # Daun Salam
    "Memiliki karakteristik pohon dengan buah manis berbentuk bulat, sering digunakan untuk jus",  # Pohon Mangga
    "Memiliki karakteristik pohon dengan buah berbentuk lonjong, kaya lemak sehat",  # Pohon Alpukat
    "Memiliki karakteristik pohon dengan buah berduri dan aroma khas, sering disebut raja buah",  # Pohon Durian
    "Memiliki karakteristik pohon dengan buah kecil berwarna merah atau kuning, kaya vitamin",  # Pohon Apel
    "Memiliki karakteristik pohon dengan buah kecil berwarna oranye, kaya vitamin C",  # Pohon Jeruk
    "Memiliki karakteristik pohon dengan buah kuning panjang berkulit lembut, sering dimakan segar",  # Pohon Pisang
    "Memiliki karakteristik pohon besar dengan buah berkulit kasar dan daging berserat",  # Pohon Nangka
    "Memiliki karakteristik pohon dengan buah bulat kecil berkulit hijau, sering dijadikan tepung",  # Pohon Sukun
    "Memiliki karakteristik pohon dengan buah kecil berwarna merah, kaya antioksidan",  # Pohon Delima
    "Memiliki karakteristik pohon dengan buah kecil manis, sering dimakan segar",  # Pohon Kersen
    "Memiliki karakteristik pohon dengan buah kecil cokelat manis, sering digunakan dalam makanan",  # Pohon Sawo
    "Memiliki karakteristik pohon dengan buah berduri kecil, kaya serat",  # Pohon Cempedak
    "Memiliki karakteristik pohon dengan buah berbulu kecil berwarna merah, manis",  # Pohon Rambutan
    "Memiliki karakteristik pohon dengan buah kecil hijau dengan daging merah muda",  # Pohon Jambu Air
    "Memiliki karakteristik pohon dengan buah bulat kecil berwarna hijau, kaya vitamin",  # Pohon Jambu Biji
    "Memiliki karakteristik pohon dengan buah lonjong berkulit hijau, kaya serat",  # Pohon Kedondong
    "Memiliki karakteristik pohon dengan buah kecil hijau, sering digunakan sebagai tepung",  # Pohon Keluwih
    "Memiliki karakteristik pohon dengan buah kecil hijau dengan rasa manis dan asam",  # Pohon Bidara
    "Memiliki karakteristik pohon besar dengan buah kecil berwarna cokelat, kaya nutrisi",  # Pohon Matoa
    "Memiliki karakteristik pohon besar dengan buah kecil berwarna cokelat manis",  # Pohon Duku
    "Memiliki karakteristik pohon besar dengan buah kecil berwarna kuning, kaya vitamin",  # Pohon Langsat
    "Memiliki karakteristik pohon dengan buah kecil berbentuk lonjong, sering digunakan untuk manisan",  # Pohon Srikaya
    "Memiliki karakteristik pohon dengan buah kecil hijau berbentuk bintang, kaya vitamin C",  # Pohon Belimbing
    "Memiliki karakteristik pohon dengan buah kecil berbentuk bulat berwarna merah, manis",  # Pohon Leci
    "Memiliki karakteristik pohon dengan buah besar berwarna ungu, rasanya manis",  # Pohon Mangosteen
    "Memiliki karakteristik pohon dengan buah kuning kecil, sering digunakan untuk bahan pangan",  # Pohon Pisang Raja
    "Memiliki karakteristik pohon dengan buah panjang berwarna kuning dan aroma khas",  # Pohon Pisang Ambon
    "Memiliki karakteristik pohon besar dengan batang penghasil nira untuk gula",  # Pohon Aren
    "Memiliki karakteristik pohon besar dengan buah manis yang sering digunakan untuk bahan baku industri",  # Pohon Kurma
    "Memiliki karakteristik pohon tinggi dengan buah kecil bulat, sering digunakan untuk minyak sawit",  # Pohon Kelapa Sawit
    "Memiliki karakteristik pohon dengan batang lurus yang digunakan untuk bahan bangunan",  # Pohon Sengon
    "Memiliki karakteristik pohon besar dengan batang kuat dan daun lebar",  # Pohon Waru
    "Memiliki karakteristik pohon besar dengan batang yang sering dianggap keramat",  # Pohon Beringin
    "Memiliki karakteristik pohon tinggi dengan batang lurus, sering digunakan untuk bahan mebel",  # Pohon Akasia
    "Memiliki karakteristik pohon tinggi dengan daun kecil dan sering digunakan sebagai kayu bakar",  # Pohon Eukaliptus
    "Memiliki karakteristik pohon tinggi dengan daun berbentuk jarum, sering digunakan untuk dekorasi",  # Pohon Cemara
]


def pencarian_linear_iteratif(katalog, karakteristik, target):
    start_time = time.perf_counter()
    for i in range(len(katalog)):
        if katalog[i].lower() == target.lower():
            end_time = time.perf_counter()
            waktu_eksekusi = end_time - start_time
            return i, waktu_eksekusi, karakteristik[i]
    end_time = time.perf_counter()
    waktu_eksekusi = end_time - start_time
    return -1, waktu_eksekusi, None

def pencarian_linear_rekursif(katalog, karakteristik, target, indeks=0, start_time=None):
    if start_time is None:
        start_time = time.perf_counter()
    if indeks >= len(katalog):
        end_time = time.perf_counter()
        waktu_eksekusi = end_time - start_time
        return -1, waktu_eksekusi, None
    if katalog[indeks].lower() == target.lower():
        end_time = time.perf_counter()
        waktu_eksekusi = end_time - start_time
        return indeks, waktu_eksekusi, karakteristik[indeks]
    return pencarian_linear_rekursif(katalog, karakteristik, target, indeks + 1, start_time)

def main():
    print("Masukkan nama-nama tanaman yang ingin dicari, dipisahkan dengan koma (,).")
    print("Contoh: Mawar,Lidah Buaya,Pandan")
    target_tanaman = input("Input: ")
    daftar_tanaman = [nama.strip() for nama in target_tanaman.split(',')]

    total_waktu_iteratif = 0
    total_waktu_rekursif = 0

    for nama_tanaman in daftar_tanaman:
        hasil_iteratif, waktu_iteratif, karakteristik_iteratif = pencarian_linear_iteratif(
            katalog_tanaman, karakteristik_tanaman, nama_tanaman
        )
        hasil_rekursif, waktu_rekursif, karakteristik_rekursif = pencarian_linear_rekursif(
            katalog_tanaman, karakteristik_tanaman, nama_tanaman
        )

        total_waktu_iteratif += waktu_iteratif
        total_waktu_rekursif += waktu_rekursif

        if hasil_iteratif != -1:
            print(f"Tanaman '{nama_tanaman}' ditemukan pada indeks {hasil_iteratif}. (Iteratif, waktu: {waktu_iteratif:.10f} detik)")
            print(f"Karakteristik: {karakteristik_iteratif}")
            print(f"Tanaman '{nama_tanaman}' ditemukan pada indeks {hasil_rekursif}. (Rekursif, waktu: {waktu_rekursif:.10f} detik)")
            print(f"Karakteristik: {karakteristik_rekursif}")
        else:
            print(f"Tanaman '{nama_tanaman}' tidak ditemukan. (Iteratif, waktu: {waktu_iteratif:.10f} detik; Rekursif, waktu: {waktu_rekursif:.10f} detik)")

    print("\n=== Rangkuman Waktu ===")
    print(f"Total waktu pencarian (Iteratif): {total_waktu_iteratif:.10f} detik")
    print(f"Total waktu pencarian (Rekursif): {total_waktu_rekursif:.10f} detik")

if __name__ == "__main__":
    main()