import unittest

from htmlnode import HTMLNode, LeafNode

#HTMLNode(self,tag,value,children,props)

class TestHTMLNode(unittest.TestCase):
    def test_not_eq_none(self):
        node = HTMLNode()
        node2 = HTMLNode(None,None,None,None)
        self.assertNotEqual(node,node2)

    def test_not_eq_tag(self):
        node = HTMLNode("p")
        node2 = HTMLNode(2)
        self.assertNotEqual(node,node2)

    def test_not_eq_value(self):
        node = HTMLNode(None, "Test")
        node2 = HTMLNode(None, " Test")
        self.assertNotEqual(node,node2)
    
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"},   )
        self.assertEqual(node.props_to_html(), ' class="greeting" href="https://boot.dev"',  )

    def test_values(self):
        node = HTMLNode("div", "I wish I could read", )
        self.assertEqual( node.tag, "div", )
        self.assertEqual( node.value, "I wish I could read", )
        self.assertEqual( node.children, None, )
        self.assertEqual( node.props, None, )

    def test_repr(self):
        node = HTMLNode( "p", "What a strange world", None, {"class": "primary"}, )
        self.assertEqual( node.__repr__(), "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})", )

    def test_leafnode_values(self):
        node = LeafNode("div", "Test value", None)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Test value")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_leafnode_to_html_value(self):
        node = LeafNode( None, "Raw Text")
        self.assertEqual(node.to_html(), "Raw Text")

    def test_leafnode_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()