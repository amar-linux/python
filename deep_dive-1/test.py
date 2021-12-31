min_len =2
name = input("Please Enter your name:")

while not (len(name) >= min_len and name.isprintable() and name.isalpha()):
    name = input("Please Enter your name:")

print("hello , {0}" . format(name))

