from sys import argv
from os.path import exists
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}...")

# Baris pertama untuk buka data dari file pertama, baris ke dua untuk baca data file yg sudah dibuka di baris pertama
in_file = open(from_file)
in_data = in_file.read()

print(">>>> data in_data:", repr(in_data))

print(f"The input file is {len(in_data)} bytes long")

print(f"Does the {exists(to_file)} exist? ")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print(f"Allright, all data from {from_file} has been read and copy to {to_file}")
out_file.close()
in_file.close()