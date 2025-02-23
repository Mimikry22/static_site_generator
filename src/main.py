from file_management import copy_files
from page_generation import generate_pages_recursive, generate_page
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files to public directory...")
    copy_files(dir_path_static,dir_path_public)
    # generate_page(
    #     os.path.join(dir_path_content, "index.md"),
    #     template_path,
    #     os.path.join(dir_path_public, "index.html"),
    # )
    print("Generating content...")
    generate_pages_recursive(
            dir_path_content, 
            template_path, 
            dir_path_public,
    )


main()