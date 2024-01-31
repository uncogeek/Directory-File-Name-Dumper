import os
from os import walk


     
         


files = []
for (dirpath, dirnames, filenames) in walk(r'C:\Users\Mr.Asgharian\Desktop\res\n'):
    files.extend(filenames)
    break

print("Files Extacted.")
print("write in txt file...")



with open('output.txt', 'w' ,encoding='utf-8') as f:
    for line in files:
        f.write("%s\n" % line)