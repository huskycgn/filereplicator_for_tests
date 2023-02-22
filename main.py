from ftplib import FTP
from cred import *

# Script for streestest

ftp_conn = FTP()

ftp_conn.connect(host=host, port=21)

ftp_conn.login(user=user, passwd=password)

counter = 0

# Testfile must exist!

try:
    with open(file='./testfile', mode='rb') as file:
        for i in range(10):
            filename = f'testfile{i+1}'
            ftp_conn.storbinary(cmd=f'STOR /anypath/{filename}', fp=file)
            print(f'wrote file: {filename}')
            counter += 1
            file.seek(0)  # Reset the file pointer to the beginning of the file

except FileNotFoundError:
    print('File does not exist!')

ftp_conn.quit()

print(f'Written {counter} files to {ftp_conn.host}')