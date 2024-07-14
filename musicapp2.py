import os  # https://docs.python.org/3/library/os.html
import hashlib  # https://docs.python.org/3/library/hashlib.html
from datetime import datetime  # https://docs.python.org/3/library/datetime.html
import subprocess  # Import subprocess to run external commands

# In-memory user database will be used to authenticate against and have two different roles.
users = {
    'user': {'password': 'user123', 'role': 'user'},
    'admin': {'password': 'admin123', 'role': 'admin'}
}

# File storage with metadata.
files = []

# Function to prompt authenticated users to match against the list of allowed users defined above.
def authenticate(username, password):
    user = users.get(username)
    if user and user['password'] == password:
        return user
    return None

# Function to generate MD5 checksum for the files uploaded, which can be viewed in view option.
def generate_md5(filename):
    md5_hash = hashlib.md5()
    try:
        with open(filename, "rb") as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                md5_hash.update(byte_block)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

# Function to handle viewing files
def view_files():
    if files:
        print(f"{'ID':<5}{'Filename':<20}{'Timestamp':<20}{'Uploader':<15}{'MD5 Checksum':<32}")
        print("="*95)
        for idx, file_info in enumerate(files, start=1):
            print(f"{idx:<5}{file_info['filename']:<20}{file_info['timestamp']:<20}{file_info['uploader']:<15}{file_info['checksum']:<32}")
        open_file_option()
    else:
        print("No files uploaded.")

# Function to handle opening files based on their type
def open_file_option():
    try:
        file_idx = int(input("Enter the number of the file to open (0 to cancel): "))
        if file_idx == 0:
            return
        if 1 <= file_idx <= len(files):
            file_to_open = files[file_idx - 1]
            filename = file_to_open['filename']
            filepath = os.path.abspath(filename)
            if filename.endswith('.mp3'):
                subprocess.run(['open', '-a', 'QuickTime Player', filepath])  # For MacOS
            elif filename.endswith('.txt'):
                subprocess.run(['open', '-a', 'TextEdit', filepath])  # For MacOS
            else:
                print("Unsupported file type.")
        else:
            print("Invalid file number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to handle uploading files which need to be available on the local computer.
def upload_file(user):
    filename = input("Enter the name of the file to upload (full path): ")
    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist.")
        return
    generate_checksum = input("Generate MD5 checksum? (y/n): ").strip().lower()
    checksum = generate_md5(filename) if generate_checksum == 'y' else "N/A"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    files.append({
        'filename': os.path.basename(filename),
        'timestamp': timestamp,
        'checksum': checksum,
        'uploader': user['username']
    })
    print(f"File '{os.path.basename(filename)}' uploaded successfully.")

# Function to handle deleting files
def delete_file(user):
    view_files()
    try:
        file_idx = int(input("Enter the number of the file to delete: "))
        if 1 <= file_idx <= len(files):
            file_to_delete = files[file_idx - 1]
            if user['role'] == 'admin' or file_to_delete['uploader'] == user['username']:
                removed_file = files.pop(file_idx - 1)
                print(f"File '{removed_file['filename']}' deleted successfully.")
            else:
                print("You do not have permission to delete this file.")
        else:
            print("Invalid file number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to display menu based on user role
def display_menu(user):
    while True:
        print("\nMenu:")
        print("1. View Artefacts")
        print("2. Upload File")
        print("3. Delete File")
        print("4. Open File")
        print("0. Logout")

        choice = input("Enter your choice: ")
        if choice == '1':
            view_files()
        elif choice == '2':
            upload_file(user)
        elif choice == '3':
            delete_file(user)
        elif choice == '4':
            open_file_option()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

# Welcome message to print some information with green color.
def print_welcome_message():
    green = "\033[92m"
    reset = "\033[0m"
    message = f"""
{green}################################################################################
################################################################################
################## (**Welcome to the Music Application Store**) ################
###########################(** University of Essex **)##########################
###########################(**     Samer Rafid Saleem     **)###################
###################(** Secure Software Design Module **)########################
################################################################################
################################################################################{reset}
    """
    print(message)

# Main function to start the application and authenticate/authorize users.
def main():
    print_welcome_message()  # Calling Welcome message function

    while True:
        username = input("Username: ")
        password = input("Password: ")

        user = authenticate(username, password)
        if user:
            user['username'] = username  # Add the username to the user dictionary for tracking
            print(f"Welcome, {username} ({user['role']}).")
            display_menu(user)
        else:
            print("Invalid credentials. Please try again.")

if __name__ == "__main__":
    main()
