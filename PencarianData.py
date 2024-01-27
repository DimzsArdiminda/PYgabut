# sqeuncey search
# number
numbers = [342,5,23,56,7]
find = 5
i = 0
# terus melakukan perulangan sesuai dengan jumlah index numbers
while i < len(numbers):
    i +=1
    break

if numbers[i] == find:
  print("ketemu di index ke - ", numbers[i])
else:
  print("ga ketemu bang")



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

# menghitung frekuensi data setiap num in numbers
# simpang dalam list kosong
for num in numb:
    count[num - min_value] +=1

# menghitung akumulasi jumlah list yang di butuhkan
for i in range(1, range_values):
    count[i] += count[i-1]

# membuat list baru
sorted_numbers = [0] * len(numb)

# pengururtan (memanfaatkan perulangan, kumpulan data, frek komulatif)
for num in numbers:
  index = count[num - min_value] - 1
  sorted_numbers[index] = num
  count[num - min_value] -= 1

print("Data sebelum diurutkan:", numbers)
print("Data setelah diurutkan:", sorted_numbers)
    
