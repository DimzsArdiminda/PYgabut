'''
ketika mengakses sebuah kolom, sekaligus menampilkaan baris
'''


# matrix 2x2
baris = [[2,3]]
kolom = [5,4]

for Mbaris in baris:
    for Ngolom in kolom:
        print([Mbaris[0]*Ngolom, Mbaris[1]*Ngolom])
    print()

# matrix 3x3

baris3 = [2, 3, 4]
kolom3 = [5, 4, 3]

for i in baris3:
    for j in kolom3:
        print([i * j, i * j, i * j])
    print()


# operasi matrix
# penjumlahan matrix
import numpy as np

# Definisi matriks A dan B
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Penjumlahan matriks
C = A + B
print("Penjumlahan matriks A dan B:")
print(C)

# Pengurangan matriks
D = A - B
print("\nPengurangan matriks A dan B:")
print(D)

# Perkalian matriks (dot product)
E = np.dot(A, B)
print("\nPerkalian matriks A dan B:")
print(E)

# Transpose matriks
F = np.transpose(A)
print("\nTranspose matriks A:")
print(F)


  
