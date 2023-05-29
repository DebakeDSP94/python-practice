# walking a directory tree

import os
import shutil
# for folderName, subfolders, filenames in os.walk('/home/stuart/Documents'):
#    print('The current folder is ' + folderName)

#   for subfolder in subfolders:
#       print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

#   for filename in filenames:
#       print('FILE INSIDE ' + folderName + ': ' + filename)

#   print('')

for foldername, subfolders, filenames in os.walk('/home/stuart/Desktop'):
    print('The current folder is ' + foldername)
    print('The subfolders in ' + foldername + ' are: ' + str(subfolders))
    print('The filenames in ' + foldername + ' are: ' + str(filenames))
    print('')

    for subfolder in subfolders:
        if 'fish' in subfolder:
           # os.rmdir(subfolder)
            print('Deleting ' + subfolder)

    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(foldername, file),
                        os.join(foldername, file + '.backup'))
