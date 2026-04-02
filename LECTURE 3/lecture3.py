import p1_random as p1
rng = p1.P1Random()
# import the module (do this on the first line of code)
# create a P1Random variable

my_number = rng.next_int(13) + 1 # A random number in range [1,13]
my_value = rng.next_int(11) + 16 # A random number in range [16,26]
print("Your card is a", my_number)
print("Your value is", my_value)

