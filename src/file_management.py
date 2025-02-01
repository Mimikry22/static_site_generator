import os
import shutil

def copy_files(dir_src, dir_dest):
    if(not os.path.exists(dir_dest)):
        os.mkdir(dir_dest)
    src_files_list = os.listdir(dir_src)
    for element in src_files_list:
        element_path = os.path.join(dir_src, element)
        dest_path = os.path.join(dir_dest, element)
        if(os.path.isdir(element_path)):
            copy_files(element_path,dest_path)
        else:
            shutil.copy(element_path, dest_path)
            print(f" * {element_path} -> {dest_path}")

