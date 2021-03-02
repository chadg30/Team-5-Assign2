# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode
from Crypto.Cipher import AES


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
    Author: David Leiden
    Inputs:
    Outputs: Displays if the username and password were stored in the file successfully
    :return:
    '''


    # encrypt password with AES algorithm
    # password to encrypt
    data = password
    # key to encrypt with
    key = get_random_bytes(16)
    print(key)
    cipher = AES.new(key, AES.MODE_CBC)
    encryped_password = cipher.encrypt(pad(data, AES.block_size))

    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(encryped_password).decode('utf-8')
    result = json.dumps({'iv': iv, 'ciphertext': ct})
    print(result)
    # store username and encypted password in the file.
    file = open('credential.dat', 'w')
    file.write(username)
    file.write(encryped_password)
    # display message.
    print("username and password saved in ", outputfile)
    #close the file
    file.close()


def main():
    vusername,vpassword=getusername_passwd()
    if vusername and vpassword:
        print(vusername)
        print(vpassword)
        secure_store(vusername, vpassword)
    else:
        print("invalid username or password")


if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
