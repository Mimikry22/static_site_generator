from file_management import copy_files

def main():
    src_dir = './static/'
    dest_dir = './public/'
    copy_files(src_dir,dest_dir)


main()