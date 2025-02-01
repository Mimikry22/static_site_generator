import os
import shutil

def copy_files(dir_src, dir_dest):
    if(not os.path.exists(dir_dest)):
        os.mkdir(dir_dest)
    else:
        shutil.rmtree(dir_dest)
        os.mkdir(dir_dest)
    src_files_list = os.listdir(dir_src)
    for element in src_files_list:
        element_path = os.path.join(dir_src, element)
        if(os.path.isdir(element_path)):
            copy_files(element_path,os.path.join(dir_dest, element))
        else:
            shutil.copy(element_path, os.path.join(dir_dest, element))


