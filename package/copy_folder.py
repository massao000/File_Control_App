import os
import shutil

def copy_folder(values, destination, name):
    shutil.copytree(values, f'{destination}/{name}')

def copy_file(values, destination, name):
    basename = os.path.basename(values)
    splitext = os.path.splitext(basename)
    shutil.copyfile(values, f"{destination}\\{name}{splitext[1]}")