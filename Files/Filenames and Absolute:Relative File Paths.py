import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
#joins the files together using the appropriate syntax for the operating system
print(os.sep) #separating method

print(os.getcwd()) #you can get the location of the current working directory

os.chdir('/Users') #changes the directory to the home directory
print(os.getcwd())

'folder1\\spam.png' # relative file path - assumed to be inside folder1 inside the current working directory

'c:\\ProgramData\\Microsoft\\....' # absolute file path assumed to be inside the root folder

os.path.abspath('spam.png') #returns the absolute path of the file that you pass it

os.path.isabs('c:\\folder\\folder') #returns true or false for the file path being absolute or not

os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')
# gives a relative path from starting path (second item in brackets) to final file (first item in brackets)

os.path.dirname('c:\\folder1\\folder2\\spam.png') #retrieves the directory part of the file path
os.path.basename('c:\\folder1\\folder2\\spam.png') #returns the last file/folder name at the end of the file path

os.path.exists('c:\\folder1\\folder2\\spam.png') #returns true or false based on whether this file path exists or not

os.path.isfile('c:\\folder1\\folder2\\spam.png') #return true or false based on whether the last item is a file or not
os.path.isdir('c:\\folder1\\folder2') #returns true or false based on whether the last item is a folder or not

os.path.getsize('c:\\folder1\\folder2\\spam.png') #returns size of file
os.listdir('c:\\folder1\\folder2') #returns the file and folder names of the items within the indicated folder

os.makedirs('Users/hey/there') #python will make these folders for you
