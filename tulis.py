from sys import argv
script, file_name = argv

print(f"Masukkan nama {file_name} tadi.")

target = open(file_name, 'w')

target.truncate()

garis1 = input("Masukkan baris ke 1: ")
garis2 = input("Masukkan baris ke 2: ")
garis3 = input("Masukkan baris ke 3: ")

print(f"Ke tiga baris sudah terisi, file {file_name} akan tersimpan.")
target.write(garis1)
target.write("\n")
target.write(garis2)
target.write("\n")
target.write(garis3)
target.write("\n")

target.close()
print("Selesai")