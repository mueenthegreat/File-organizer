import os
import shutil
from pathlib import Path

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def organize_files():
    DIRECTORIES = {
        "DOCUMENTS": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "IMAGES": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "VIDEOS": [".mp4", ".mkv", ".avi", ".mov"],
        "MUSIC": [".mp3", ".wav", ".flac"],
        "ARCHIVES": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "CODE": [".py", ".java", ".cpp", ".html", ".css", ".js"]
    }
    current_dir = os.getcwd()

    for folder_name in DIRECTORIES:
        create_folder(os.path.join(current_dir, folder_name))


    for file in os.listdir(current_dir):
        if os.path.isfile(file):

            file_ext = os.path.splitext(file)[1].lower()

            for folder_name, extensions in DIRECTORIES.items():
                if file_ext in extensions:

                    source = os.path.join(current_dir, file)
                    destination = os.path.join(current_dir, folder_name, file)
                    shutil.move(source, destination)
                    print(f"Moved {file} to {folder_name}")
                    break

if __name__ == "__main__":
    organize_files()
    print("File organization completed!")
