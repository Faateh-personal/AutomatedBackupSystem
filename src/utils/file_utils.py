import os


def list_files_in_directory(directory_path):
    """Lists all files in a given directory."""
    file_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def check_file_changes(file_path, last_modified_time):
    """Checks if a file has been modified since the last backup."""
    current_modified_time = os.path.getmtime(file_path)
    return current_modified_time > last_modified_time
