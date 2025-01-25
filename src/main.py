from textnode import *
from htmlnode import HTMLNode

def main():
    test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(test)
    attr_tag = {
    "href": "https://www.google.com",
    "target": "_blank",
    }
    test_node = HTMLNode("p","string", ["a","b"], attr_tag)
    print(test_node.props_to_html())
    print(type(test_node.props_to_html()))

main()