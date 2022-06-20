from sys import argv

script, file_name = argv

print(f"Masukkan nama {file_name}")
print("Lanjut apa nggak?")

target = open(file_name, 'w')

target.truncate()
print(target)

line1 = input("Masukkan line1: ")
line2 = input("Masukkan line2: ")
line3 = input("Masukkan line3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()