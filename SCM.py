'''
Date: 3/2/2021
Authors: Chad Green, David Leiden, Jenna Josselyn

SCM takes a users password and username
'''

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES


def getusername_passwd():
    '''
    Author: Chad Green
    Inputs:
    Outputs: Returns valid username and password entered by a user
    '''
    valuser=False
    valpass=False

    sym = ['#', '@', '%', '*']

    username = input("Enter username: <email address> ")
    if "@" in username and ".com" in username:
        valuser=True
    else:
        valuser=False

    password = input("Enter your password. Enter at least 8 characters, with at least "
                     "one uppercase letter, one lowercase letter, one number, and a character from [#,$,%,*]\n")
    while not valpass:
        if len(password) >= 8:
            valpass=True
        else:
            valpass=False
            break
        if any(char.isupper() for char in password):
            valpass=True
        else:
            valpass=False
            break
        if any(char.islower() for char in password):
            valpass = True
        else:
            valpass=False
            break
        if any(char.isdigit() for char in password):
            valpass = True
        else:
            valpass=False
            break
        if any(char in sym for char in password):
            valpass=True
        else:
            valpass=False
            break

    if valpass and valuser:
        return username, password
    else:
        return None, None

    
def secure_store(username, password):
    '''
    Author: David Leiden/Chad Green
    Inputs: username and password
    Outputs: Displays if the username and password were stored in the file successfully
    '''

    # encrypt password with AES algorithm
    # password to encrypt
    data = password
    # key to encrypt with
    key = get_random_bytes(16)
    # create the cypher
    cipher = AES.new(key, AES.MODE_EAX)
    # encrypt the password
    encrypted_password = cipher.encrypt(password.encode('utf-8'))
    # store username and encypted password in the file.
    file = open('credential.dat', 'a')
    file.write(username + '\n')
    file.write(str(encrypted_password) + '\n')
    # display message.
    print("username and password saved in credentials.dat")
    # close the file
    file.close()


def main():
    vusername,vpassword=getusername_passwd()
    if vusername and vpassword:
        secure_store(vusername, vpassword)
    else:
        print("invalid username or password")


if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
