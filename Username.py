import random

# Imports above

# Do not change these lists!
characters = "abcdefghijklmnoprstuvyzxqw0123456789"
symbols = "!+.,;:=?_-|"


# Do not change these lists!

benim = "oldmcdonaldshadafarm"
letter = random.choice(benim[0:6])
print(letter)


def create_username():
    long = int(input("how long do you want your username to be? "))
    while long > 20 or long < 5:
        long = int(input("how long do you want your username to be? "))
    sosc = input("Which social media platform you'll be using it for")
    username = sosc[0:2] + random.choice(symbols)
    if long > 5 and long < 20:
        username = username + random.choice(characters)
    print(username)




def create_password():
    pass


def main():
    create_username()
    username = create_username()
    password = create_password()
    print("Your username is:", username)
    print("Your password is:", password)


main()



create_username()

