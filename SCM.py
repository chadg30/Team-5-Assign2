# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def getusername_passwd():
    valuser=False
    valpass=False

    sym = ['#', '$', '%', '*']

    username = input("Enter username: <email address> ")
    while not valuser:
        if "@" in username and ".com" in username:
            valuser=True
        else:
            username = input("Incorrect, try again: ")

    while not valpass:
        password = input("Enter your password. Enter at least 8 characters, with at least "
                         "one uppercase letter, one lowercase letter, one number, and a character from [#,$,%,*]\n")
        if len(password) > 8:
            valpass=True
        else:
            valpass=False
        if any(char.isupper() for char in password):
            valpass=True
        else:
            valpass=False
        if any(char.islower() for char in password):
            valpass = True
        else:
            valpass=False
        if any(char.isdigit() for char in password):
            valpass = True
        else:
            valpass=False
        if any(char in sym for char in password):
            valpass=True
        else:
            valpass=False

    return username, password


def main():
    vusername,vpassword=getusername_passwd()
    print(vpassword)
    print(vusername)


if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
