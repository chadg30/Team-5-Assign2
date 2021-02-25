# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def getusername_passwd():
    valuser=False
    valpass=False

    username = input("Enter username: <email address> ")
    while not valuser:
        if "@" in username and ".com" in username:
            valuser=True
        else:
            username = input("Incorrect, try again: ")

    while not valpass:
        password = input("Enter your password. Enter at least 8 characters, with at least "
                         "one letter, one number, and a character from [#,$,%,*]\n")
        if "#" in password or "$" in password or "%" in password or "*" in password:
            valpass=True

    return username, password


def main():
    vusername,vpassword=getusername_passwd()
    print(vpassword)
    print(vusername)


if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
