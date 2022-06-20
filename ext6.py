x = 'There are %d types of people' % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)
print("\n" * 2)

print("I said: %r." % x) #dengan %r variabel akan ditulis utuh (raw) lengkap dengan tanda quote(" ")
print('I said also "%s".' % y) # dengan %s tanda quote harus ditulis ulang jika dikehendaki ada tanda quote
print("\n" * 2)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)
print("\n" * 2)

w = "This is the left side of... "
e = "a string with the right side."

print(w + e)