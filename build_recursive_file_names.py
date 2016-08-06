from os import walk
from os.path import split, splitext, join, exists

def select_files(root, files, extensions=[]):
    """
    simple logic here to filter out interesting files based on extensions
    """

    selected_files = []

    for file in files:
        #do concatenation here to get full path 
        full_path = join(root, file)
        ext = splitext(file)[1]

        if len(extensions) == 0 or ext in extensions:
            selected_files.append(full_path)

    return selected_files

def build_recursive_dir_tree(path, ext=[]):
    """
    path    -    where to begin folder scan
    """
    selected_files = []

    for root, dirs, files in walk(path):
        selected_files += select_files(root, files, extensions=ext)

    return selected_files
    
list = build_recursive_dir_tree('c:\\temp')
print (list)