import os

folderName = input("Enter the folder path: ")

# Enter folder pathname as string
for folderName, subfolders, filenames in os.walk(folderName):
    """Displays the entire directory tree of file path you enter"""
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE: ' + folderName + ': ' + filename)

    print('')
