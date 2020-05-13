import shutil

shutil.copy("c://spam.txt", 'c:\\delicious') #copies the file to the second stated destination folder
shutil.copy("c://spam.txt", 'c:\\delicious\\spamspamspam.txt') #copies the file to the second stated destination folder and changes its name

shutil.copytree('c:\\delicious', 'c:\\delicious_backup') #a copy of the delicious folder will be created with its contents

shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut') #move the file to the new location
shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut\\newName.txt') #move the file to the new location and give it a new name
