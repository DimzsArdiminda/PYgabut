def gabungNamaNilai(nama, nilai):
    return list(zip(nama, nilai))
# def tampilkanData(data):
#     for nama, nilai in data:
#         print(f"Nama {nama} nilai {nilai}")

print("""
      Selamat datang di Program untuk memasukkan nilai Peserta didik ke dalam sebuah variabel \n
      
      Keterangan:
      1. Masukkan jumlah murid + 1. Misal, jika murid Anda sebanyak 40, maka masukkan 41\n
      2. Data murid ke-0 bersifat abstrak (tidak jelas), tetapi harus dan wajib diisi\n
      """)

# Step 1: Meminta jumlah murid
jumlah_murid = int(input("Masukkan jumlah murid: "))

# Step 2: Melakukan perulangan sesuai jumlah murid dan memasukkannya ke dalam array
nama_murid = []
nilai_murid = []
for i in range(jumlah_murid):
    print(f"\nData murid ke-{i+1}")
    nama = input("Masukkan Nama murid: ")
    nilai = int(input("Masukkan Nilai Murid: "))
    nama_murid.append(nama)
    nilai_murid.append(nilai)

# Step 3: Menggabungkan data nama dan nilai
data_murid = gabungNamaNilai(nama_murid, nilai_murid)

# Step 4: Menampilkan data yang ada
# tampilkanData(data)

for nama, nilai in data_murid:
    print(f"Nama {nama}, nilai {nilai}")
    
    
