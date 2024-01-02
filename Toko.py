# membuat program "keranjang sederhana"
#masih perlu optimze


keranjang = {
    "makanan" : 0,
    "minuman" : 0,
}


def menu():
    print("""masukan pilihan anda \n
    a. makanan
    b. minuman
    """)
    pilihan = str(input("masukan pilihan anda: "))
    if pilihan == 'a' or pilihan == "a. makanan":
        keranjang["makanan"] += 1
        print("Bismillah, berhasil ditambahkan ke keranjang!")
        
        
    
while True:
    print("""
    selamat datang \n
    silahkan memilih \n
    1. masuk ke menu \n
    2. tampilkan belanjaan \n
    """)
    
    pilihan_pertama = int(input("masukan pilihan anda : "))
    if pilihan_pertama == 1:
        menu()
    elif pilihan_pertama == 2:
        print("makanan : ",keranjang["makanan"],
        "\n", "minuman : ", keranjang["minuman"])
    else:
        continue
    
    
    
