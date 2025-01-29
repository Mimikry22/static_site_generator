import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    #text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    #text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    matches = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
def split_nodes_image(old_nodes):
    new_nodes = []
    sections_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_images(old_node.text)
        section_text = old_node.text
        if len(matches) == 0:
            new_nodes.append(old_node)
            continue
        for match in matches:
            sections_list = section_text.split(f'![{match[0]}]({match[1]})',1)
            if len(sections_list) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections_list[0] != "":
                new_nodes.append(TextNode(sections_list[0], TextType.NORMAL))
            new_nodes.append(TextNode(match[0], TextType.IMAGES, match[1]))
            section_text = sections_list[1]
        if section_text != "":
            new_nodes.append(TextNode(section_text, TextType.NORMAL))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    sections_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_links(old_node.text)
        section_text = old_node.text
        if len(matches) == 0:
            new_nodes.append(old_node)
            continue
        for match in matches:
            sections_list = section_text.split(f'[{match[0]}]({match[1]})',1)
            if len(sections_list) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections_list[0] != "":
                new_nodes.append(TextNode(sections_list[0], TextType.NORMAL))
            new_nodes.append(TextNode(match[0], TextType.LINKS, match[1]))
            section_text = sections_list[1]
        if section_text != "":
            new_nodes.append(TextNode(section_text, TextType.NORMAL))
    return new_nodes
