import os

os.unlink('bacon.txt') #this file will be permanently deleted
os.rmdir("c:\\folderName") #remove a specific folder, but the folder must be empty for it to delete

import shutil
shutil.rmtree('c:\\delicious') #deletes a folder and all its content

import send2trash
send2trash.send2trash('c:\\users\\desktop\\file.rxt')
