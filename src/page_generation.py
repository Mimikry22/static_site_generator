from markdown_blocks import extract_title, markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(os.path.join(from_path)) as file:
        md_content = file.read()

    #print(md_content)

    with open(os.path.join(template_path)) as file:
        template_content = file.read()

    #print(template_content)
    html_node = markdown_to_html_node(md_content).to_html()
    #print(type(html_node))
    html_title = extract_title(md_content)
    #print(html_title)
    new_content = template_content.replace("{{ Title }}", html_title)
    new_content = new_content.replace("{{ Content }}", html_node)

    dest_dir_path = os.path.dirname(dest_path)
    if (dest_path != ""):
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(new_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if(not os.path.exists(dest_dir_path)):
        os.mkdir(dest_dir_path)
    src_files_list = os.listdir(dir_path_content)
    for element in src_files_list:
        element_path = os.path.join(dir_path_content, element)
        dest_path = os.path.join(dest_dir_path, element)
        if(os.path.isdir(element_path)):
            generate_pages_recursive(element_path,template_path,dest_path)
        else:
            generate_page(element_path,template_path, dest_path.replace(".md", ".html"))
            print(f" * {element_path} -> {dest_path}")
