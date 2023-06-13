# Folder Item Display
This Python script allows you to display the items (files and folders) within a specified root folder and its subfolders. It provides a count of the total number of files and folders found.

## Requirements
- Python 3.x
- os module (part of the Python standard library)
## Usage
- Modify the root_folder variable in the main function to specify the root folder path from where you want to start displaying the items. For example, if you want to display items starting from the "C:" drive, set root_folder = "C:\\".
- Run the script using a Python interpreter.
- The script will iterate through every other folder within the root folder and display the files and folders found.
- It will also print the total number of files and folders.

## Code Explanation
The script consists of the following main components:

1. display_items_in_folder(folder_path): This function takes a folder path as input and recursively displays the files and folders within that folder. It uses the os.listdir function to get the list of items in the folder and checks whether each item is a file or a folder. For files, it prints "File: <filename>" and increments the file counter. For folders, it recursively calls itself with the subfolder path and adds the returned file and folder counts to the counters.

2. main(): This function is the entry point of the script. It sets the root_folder variable to specify the root folder path and initializes the total file and folder counters. It then iterates through every other folder within the root folder using os.listdir. For each folder, it calls the display_items_in_folder function to display the items and updates the total file and folder counters accordingly.

3. __name__ == '__main__' block: This block ensures that the main() function is only executed when the script is run directly (not imported as a module).

## Error Handling
The script includes error handling to catch any OSError exceptions that may occur when accessing a folder. If an error occurs, it will print an error message indicating the folder path and the specific error message.

### Note: It's recommended to handle errors more gracefully in a production environment, such as logging the error or providing a user-friendly error message.