import os

totalSize = 0
# linux
for filename in os.listdir('/home/stuart'):
    totalSize = totalSize + \
        os.path.getsize(os.path.join('/home/stuart', filename))
print(totalSize)
