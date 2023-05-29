# copying and moving files in python

import os
import shutil
import send2trash
from pathlib import Path
dataFolder = Path('/home/stuart/Documents')
# copy file
shutil.copy(dataFolder / 'bacon.txt', dataFolder / 'bacon_copy.txt')
# copy folder
shutil.copytree(dataFolder / 'bacon', dataFolder / 'bacon_backup')
# move file
shutil.move(dataFolder / 'bacon.txt', dataFolder / 'bacon_backup.txt')
# rename file
shutil.move(dataFolder / 'bacon_copy.txt', dataFolder / 'bacon.txt')
# delete file
shutil.rmtree(dataFolder / 'bacon_backup.txt')
# safe delete file
send2trash.send2trash(dataFolder / 'bacon.txt')
send2trash.send2trash(dataFolder / 'bacon_backup')

# walking a directory tree
# Compare this snippet from walking_directory_tree.py:

for folderName, subfolders, filenames in os.walk('/home/stuart/Documents'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')

os.unlink('/home/stuart/Documents/bacon.txt')
os.unlink('/home/stuart/Documents/bacon_backup.txt')
os.unlink('/home/stuart/Documents/bacon_copy.txt')
os.rmdir('/home/stuart/Documents/bacon')
os.rmdir('/home/stuart/Documents/bacon_backup')
os.rmdir('/home/stuart/Documents/bacon_backup/bacon')
