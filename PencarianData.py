# counting sort
''' 
mengurutkan data dari terkecil sampai ke yang terbesar

step 1: membuat slot kosong
step 2 : menghitung frekuensi
step 3 : memisahkan data 
step 4 : pengurutan
'''
# inisialisasi angka
numb = [5,5,3,5,13,5,4,3,2,1]

# tentukan rentang nilai dari kumpulan data
'''
nilai max - nilai min + 1 => untuk mencari
rentang nilai dari kumpulan data
'''
max_value = max(numb)
min_value = min(numb)
range_values = max_value - min_value +1

# membuat list kosong
count = [0] * range_values
