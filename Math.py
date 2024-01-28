# membuat perulangan bersarang

def prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True
    
def masukanAngka(atas):
    list_prima = []
    for angka in range(2 , atas+1):
        if prima(angka):
            list_prima.append(angka)
    return list_prima
    


atas = int(input("masukan batas atas bilangan prima "))
if atas >= 2:
    x = masukanAngka(atas)
    print(f'angka yang termasuk dalam bilangan prima antara 2 sampai dengan {atas} adalah {x}' )
else:
    print('eror')


# faktorial 
# kode faktorial
# f(5) = 5 * 4 * 3 * 2 * 1
# f(5) = 15

fib = 3
num = 1
for i in range(fib,1,-1):
  num = num * i
  print(num)
