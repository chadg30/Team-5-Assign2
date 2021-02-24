# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def getusername_passwd():
    username=input("Enter username: <email address>")
    password=input("Enter your password. Enter at least 8 characters, with at least "
                   "one letter, one number, and a character from [#,$,%,*]\n")
    return username, password


def main():
    vusername,vpassword=getusername_passwd()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
