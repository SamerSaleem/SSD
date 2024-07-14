# SSD
Download the code file named "musicapp2.py"
once downloaded, open VSCODE or any IDE and run the code.
or you can do this from Linux Sheel or MAC terminal or Windows CMD.
you will need the following libraries:
1. hashlib  >>>> External Library, check below how to install.
2. OS
3. datetime

so you can import these with the following commands from your terminals:
pip install package-name
example:
pip install hashlib
after this, you should be able to run the application without problems.
then you can select the users you want to login with
1. username= user password= user123 (can view, upload, and delete his own data only)
2. username= admin password= admin123 (can upload, view, delete, update)
3. you can use the upload to files temporarily into memory which you can view the files you uploaded
4. the files must be uploaded using real path from your local PC in my case "/home/samer/test.mp3" need to be entered into the CLI when prompted by the APP.
5. you can view the files after uploading or delete them and any view will show checksum value generated with timestamp and user uploaded the files.
   
# Music Application Store

This is a simple command-line application for managing and viewing files with basic user authentication. It supports file encryption and decryption using AES encryption.

# Features

- User authentication with two roles: `user` and `admin`
- Upload files with optional encryption
- View files with metadata (filename, timestamp, uploader, checksum)
- Open files with optional decryption
- Delete files with role-based access control

# Prerequisites

- Python 3.6 or higher
- `pycryptodome` library for AES encryption

# Installation

1. **Clone the repository:**
   ```bash https://github.com/SamerSaleem/SSD
   git clone https://github.com/SamerSaleem/SSD/musicapp.py
   cd SSD

2. pip install pycryptodome
3. run the code in your local computer python3.10 musicapp.py

4. Authentication
You will be prompted to enter your username and password. The default credentials are:

User:
Username: user
Password: user123
Admin:
Username: admin
Password: admin123

5. Menu Options
After logging in, you will see the following menu:

View Artefacts: Display a list of uploaded files with their metadata.
Upload File: Upload a new file with optional encryption.
Delete File: Delete an existing file (Admins can delete any file, users can delete only their own files).
Open File: Open an existing file with optional decryption.
Logout: Log out of the application.
Encryption and Decryption
Encryption: When uploading a file, you will be prompted to choose if you want to encrypt the file. If you choose y, the file will be encrypted using AES.
Decryption: When opening a file, you will be prompted to choose if you want to decrypt the file before opening. If you choose y, the file will be decrypted before opening.
Re-encryption: After viewing a decrypted file, you will be prompted to choose if you want to re-encrypt the file.

Example:

Upload a File:

Choose option 2 from the menu.
Enter the full path of the file to upload.
Choose whether to encrypt the file (y/n).
Choose whether to generate an MD5 checksum (y/n).
View Files:

Choose option 1 from the menu to see a list of uploaded files.
Open a File:

Choose option 4 from the menu.
Enter the number of the file to open.
Choose whether to decrypt the file before opening (y/n).
Choose whether to re-encrypt the file after viewing (y/n).
Delete a File:

Choose option 3 from the menu.
Enter the number of the file to delete.
Notes

Ensure that the AES key is kept secure and private.
The AES key used in this application is hardcoded for simplicity. In a production environment, use a more secure key management solution.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements

This project was developed as part of the Secure Software Design Module at the University of Essex.

Disclaimer: This application is for educational purposes only. Do not use it to handle sensitive data in a production environment without proper security audits and improvements.


