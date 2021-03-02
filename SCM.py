# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def getusername_passwd():
    '''
    Author: Chad Green
    Inputs:
    Outputs: Returns valid username and password entered by a user
    '''
    valuser=False
    valpass=False

    sym = ['#', '$', '%', '*']

    username = input("Enter username: <email address> ")
    if "@" in username and ".com" in username:
        valuser=True
    else:
        valuser=False

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

    if valpass and valuser:
        return username, password
    else:
        return None, None

def secure_store(username, password):
    '''
    Author:
    Inputs:
    Outputs:
    :return:
    '''
    outputfile = "credential.dat"
    fd = open(outputfile, 'ra')

    # encrypt password with AES algorithm
    encrypted_password = ''
    # store username and encypted password in the file.
    file = open('credential.dat', 'w')
    file.write(encryped_password)
    file.close()
    # display message.
    print("username and password saved in ", outputfile)


def main():
    vusername,vpassword=getusername_passwd()
    if vusername and vpassword:
        print(vusername)
        print(vpassword)
    else:
        print("invalid username or password")


if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
