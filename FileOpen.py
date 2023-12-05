import os
import subprocess

def open_files(file_paths):
    for file_path in file_paths:
        try:
            # Use the default application associated with the file type
            os.startfile(file_path)
        except AttributeError:
            try:
                # For Linux-based systems
                subprocess.run(['xdg-open', file_path])
            except FileNotFoundError:
                print(f"Unable to open {file_path}. Please open it manually.")

if __name__ == "__main__":
    # Specify the list of file paths you want to open
    files_to_open = [
        'path/to/file1.txt',
        'path/to/file2.jpg',
        'path/to/file3.pdf',
        # Add more file paths as needed
    ]

    open_files(files_to_open)
