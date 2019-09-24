import os

for filename in os.listdir():
    if '.access' in filename:
        fi = filename.replace('.access', '')
        os.rename(filename, fi)