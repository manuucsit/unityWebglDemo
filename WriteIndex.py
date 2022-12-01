import os

folders = os.listdir()
folders.remove('.git')

print(folders)