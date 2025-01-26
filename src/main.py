from textnode import *
from htmlnode import HTMLNode, LeafNode

def main():
    test_text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(test_text_node)
    attr_tag = {
    "href": "https://www.google.com",
    "target": "_blank",
    }
    test_html_node = HTMLNode("p","string", ["a","b"], attr_tag)
    #print(test_html_node.props_to_html())
    #print(type(test_html_node.props_to_html()))
    #print(test_html_node)
    test_leaf_node1 = LeafNode("p", "This is a paragraph of text.")
    test_leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(test_leaf_node1.to_html())
    print(test_leaf_node2.to_html())

main()