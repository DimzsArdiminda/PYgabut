nama = str(input("masukan nama anda: ")).upper()
konsonan = ["A", "I","U", "E", "O"]

list_konsonan = {
    "A" : 0,
    "I" : 0,
    "U" : 0,
    "E" : 0,
    "O" : 0
}

for huruf in nama:
    if huruf in konsonan:
        list_konsonan[huruf] += 1

print("Huruf yang ada di dalam alfabet konsonan adalah:")
for konsonan, jumlah in list_konsonan.items():
    print(f"{konsonan} : {jumlah}")
