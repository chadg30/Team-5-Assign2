'''
Author: Naresh Adhikari, Sru
This is a skeletal program that students need to implement the declared
and defined functions under @TODO annotation, according to the logic/functional requirements stated in assigment-2.pdf.

Students are not expected to midify main() function.
'''
import hashlib


def secure_hashed_passwd(username, passwd):
    import hashlib, uuid
    import os

    '''
    @TODO: Students are required to implement this function.
    using salt+pepper+sha3-224 algorithm
    :param username: string repr of username
    :param passwd: a plain text password
    :return: True if given values are stored successfully in outfile var; else returns False
    '''
    sha = hashlib.sha3_224()

    # Add salt
    salt = uuid.uuid4().hex
    # add pepper
    pepper = uuid.uuid4().hex
    # use salt and pepper to hash 'hpasswd' using sha-3-224 algorithm
    passwd.encode('utf-8')
    sha.update(bytes(salt, 'utf-8') + bytes(pepper, 'utf-8') + bytes(passwd, 'utf-8'))
    # return salt,pepper,saltpepperdigest
    return salt, pepper, sha.hexdigest()


def verify_hashed_passwd(username, passwd):
    '''
    @TODO: Students are required to implement this function.

    Server side verifies login credentials username and password
    :param username:
    :param hpasswd:
    :return:
    '''
    #databse file with username and hashed-password.
    infile="hlogins.dat"
    #open the file to read
    fd=open(infile,"r")
    #read the infile line by line to retrive a matching row with first field value of username

    match = False
    sha3 = hashlib.sha3_224()


    for line in fd:
        c = line.split(',')
        if username in line:
            match = True
            salt = c[1]
            pepper = c[2]
            hpass = c[3]

            sha3.update(bytes(salt, 'utf-8') + bytes(pepper, 'utf-8') + bytes(passwd, 'utf-8'))
            temppass = sha3.hexdigest()

    if match:
        if temppass == hpass:
            return True
        else:
            return False

    #To read the file line by line, use a for loop.
    #Hint: split each line by a comma "," to get list of username, salt, pepper, and stored_hashpassword values.
    #implement other logics inside loop.
    fd.close()

def main():
    '''Do not modify this function.'''

    import hashlib, uuid
    import os

    lusername=["shyamal@gmail.com",
                "brutforce@yahoo.com",
                "lifegivesalot@protonmail.com",
                "rainbow@sru.edu",
                "ghana@makai.com",
                "david@inst.edu",
                "buttlerbusiness@sru.edu",
                "myChurch45@state.edu"]
    lpasswd=["pass$1290Red",
            "fail$567Blue",
            "rainB0w159$",
            "lglot$$$Tatoo",
            "ghana456$$909",
            "DavI0234$09",
            "IsBulltop345",
            "xCrosTop24"]

    # open file outfile in write mode.
    outfile="hlogins.dat"
    fd = open(outfile, "w+")
    #@server: call method for each usernames, passwords.
    for i in range(0,len(lusername)):
        username=lusername[i]
        passwd=lpasswd[i]
        salt,pepper,saltpepperdigest=secure_hashed_passwd(username,passwd)
        if i in [3,7,1]:continue
        fd.write(username + "," + str(salt) + "," + str(pepper) + "," + saltpepperdigest+","+"$\n")
    fd.close()

    for j in range(0,len(lusername)):
        uname=lusername[j]
        passwd=lpasswd[j]
        result=verify_hashed_passwd(uname,passwd)
        if not result:
            print("<!> Login failed for user ",uname)
        else:
            print("Login succesful for user ",uname)

if __name__ == "__main__":
    main()