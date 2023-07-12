from ftplib import FTP
from credentials import *

# Script for streestest

ftp_conn = FTP()

ftp_conn.connect(host=host, port=21)

ftp_conn.login(user=user, passwd=password)

counter = 0

# Testfile must exist!

try:
    with open(file=f'./{srcfilename}', mode='rb') as file:
        for i in range(400):
            filename = f'{srcfilename}'
            filename_name = filename.split('.')[0]
            filename_suffix = filename.split('.')[1]
            new_filename = filename_name + f'_{i+1}' + '.' + filename_suffix
            filename = new_filename
            ftp_conn.storbinary(cmd=f'STOR {destpath}{filename}', fp=file)
            print(f'wrote file: {filename}')
            counter += 1
            file.seek(0)  # Reset the file pointer to the beginning of the file
#
except FileNotFoundError:
    print('File does not exist!')

ftp_conn.quit()

print(f'Written {counter} files to {ftp_conn.host}')