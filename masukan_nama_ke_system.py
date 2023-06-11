#  * 1. meminta user untuk memasukan berapa jumlah murid, digunkan untuk mengatur berapa kali iterasi berjalan
#  * 2. menerima nama murid dan nilai dari user dan memasukannya ke dalam array
#  * 3. menggabungkan 2 tipe data (Nama (str) Nilai (int)) 
#  * 4. menampilkan setipa data yang ada

# menggabungkan 2 tipe data, nilai dan nama 
def gabungNamaNilai(nama, nilai):
    return list(zip(nama,nilai))

def tampilkanData(data):
    for nama, nilai in data:
        print(f"Nama {nama} nilai {nilai}")

print("""
      Selamat datang di Program untuk memasukan nilai Peserta didik ke dalam sebuah variabel \n
      
      Keterangan 
      1. Masukan jumlah murid + 1 misal, jika murid anda sebanyak 40, maka masukan  41\n
      2. Data murid ke 0 bersifat abstrak (tidak jelas), tetapi harus dan wajib diisi\n
      """)

# step 1 meminta jumlah murid
jumlah_murid = int(input("masukan jumlah murid: "))
# steo 2  melaukakn perulangan sesuai jumlah murid dan memasukaknnya ke dalam array
nama_murid = []
nilai_murid = []
for i in range(jumlah_murid):
    print(f"\ndata murid ke {i}")
    nama = input("Masukan Nama murid: ")
    nilai = int(input("Masukan Nilai Murid: "))
    nama_murid.append(nama)
    nilai_murid.append(nilai)

data_murid = gabungNamaNilai(nama_murid, nilai_murid)
tampilkanData(data_murid)
