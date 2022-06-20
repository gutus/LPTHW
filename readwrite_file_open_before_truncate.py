from sys import argv
script, file_name = argv

print(f"Put your file name {file_name}")
print("We will check the file, if it is available.")

target = open(file_name, 'r')
print("We will truncate the file!")
target.read()
target.truncate()
print("Now give me 3 new lines for the file")

line1 = input(str("Put the 1st line. \n "))
line2 = input(str("Put the 2nd line. \n"))
line3 = input(str("Put the 3rd line. \n"))

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Now it has done with 3 new lines.")
target.close()
target = open(file_name, 'r')
print(target.read())

