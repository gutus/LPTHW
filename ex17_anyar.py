from sys import argv
from os.path import exists

script, dari_file, ke_file = argv

print(f" Copy  dari {dari_file} ke file {ke_file}")
in_file = open(dari_file)
in_data = in_file.read()

print(f"Apakah file {dari_file} exist? Ternyata {exists(dari_file)}")
print(f"Ternyata data {dari_file} memiliki {len(data_dari)}")

print("Lanjut atau tidak? Tekan ENTER untuk lanjut.")
input()

file_copy = open(ke_file, "w")
file_copy.write(data_dari)

print(f"Data dari {dari_file} berhasil di-copy ke {ke_file}")

data_dari.close()
file_copy.close()
