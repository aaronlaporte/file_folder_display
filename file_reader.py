import os

def display_items_in_folder(folder_path):
    file_counter = 0
    folder_counter = 0
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                print("File:", item)
                file_counter += 1
            elif os.path.isdir(item_path):
                print("Folder:", item)
                sub_files, sub_folders = display_items_in_folder(item_path)
                file_counter += sub_files
                folder_counter += sub_folders
                folder_counter += 1
    except OSError as e:
        print("Error accessing folder:", folder_path)
        print("Error message:", str(e))
    return file_counter, folder_counter

def main():
    # Set the root folder path from where you want to start displaying the items
    root_folder = "C:\\"  # Change this to your desired root folder

    total_files = 0
    total_folders = 0

    # Iterate through every other folder within the root folder
    for index, folder in enumerate(os.listdir(root_folder)):
        if index % 2 == 0:
            folder_path = os.path.join(root_folder, folder)
            print("Processing folder:", folder_path)
            sub_files, sub_folders = display_items_in_folder(folder_path)
            total_files += sub_files
            total_folders += sub_folders
            total_folders += 1

    print("Total files:", total_files)
    print("Total folders:", total_folders)

if __name__ == '__main__':
    main()
