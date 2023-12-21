# nama = str(input("masukan nama anda "))

# dictioanry
data_diri = {
    "input_nama" : "nama"
}
# print(data_diri["input_nama"])
 
array_random = [15,"mangga"]
# print(array_random)
# print(array_random[1])

# mengubah huruf besar ke kecil dan sebaliknya
kataKecil = "BISMILLAH"
kataKecil= kataKecil.lower()
# print(kataKecil)

# asal = str(input("masukan asal anda ")).upper()
# print(asal)

# menghapus space kanan dan kiri kalimat
print("dimas   ".rstrip())
print("   dimas".lstrip())
print("dimas ardiminda".strip("dimas"))
# penggabungan
print(' '.join(['Dimas','ardiminda', '!']))

# split
print("dimas ardiminda".split())

# memberikan nama untuk multiple
lista = ['kemeja', 'ungu', 'M']
apparel, color, size = lista

print(lista, apparel, color, size)

# pengurutan data
merek_motor = ['Ducati', 'harly', 'BMX', 'hONDA']
merek_motor.sort()
# merek_motor.sort(reverse=True)

print(merek_motor)

    
