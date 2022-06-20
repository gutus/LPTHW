#Conth script argumen
def print_dua(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, sedangkan arg2: {arg2}")

def print_dua_lagi(arg1, arg2):
    print(f"arg1: {arg1}, sedangkan arg2: {arg2}")

def print_satu(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("Ini kosong.")

print_dua("Gutus ","Nirwanto")
print_dua_lagi("Gutus ","Nirwanto")
print_satu("Satu!")
print_none()