from sys import argv
script, first, second, third = argv
#dari sys impor argument variable

print(">>>> argv = ", repr(argv))
#di atas digunakan untuk debugging, reprint(nama fungsi yg hendak di debug)
print("Is ini adalah teks pertama :", first)
print("Nah kalo yang ini teks kedua :", second)
print("Nah ini penutup ke tiga :", third)