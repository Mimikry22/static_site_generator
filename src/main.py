from textnode import *
from htmlnode import HTMLNode

def main():
    test_text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(test_text_node)
    attr_tag = {
    "href": "https://www.google.com",
    "target": "_blank",
    }
    test_html_node = HTMLNode("p","string", ["a","b"], attr_tag)
    #print(test_node.props_to_html())
    #print(type(test_node.props_to_html()))
    print(test_html_node)

main()