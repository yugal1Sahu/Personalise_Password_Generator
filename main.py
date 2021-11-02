import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "123456789"
symbols = "!@#$%^&*()_+-={}|:;<>,./?"
#upper, lower, nums, syms = True, True, True, True
upper = int(input("Want to include upper case letter into your password? If yes give 1\n"))

lower = int(input("Want to include lower case letter into your password? If yes give 1\n"))

nums = int(input("Want to include digits into your password? If yes give 1\n"))

syms = int(input("Want to include Special letters into your password? If yes give 1\n"))




all = ""

if upper == 1:
    all += uppercase_letters
if lower == 1:
    all += lowercase_letters
if nums == 1:
    all += digits
if syms == 1:
    all += symbols

length = int(input("What length of password you want?\n"))

amount = int(input("Numbers of sugggested password you required\n"))

for a in range(amount):
    password = "".join(random.sample(all,length))
    print(password)



