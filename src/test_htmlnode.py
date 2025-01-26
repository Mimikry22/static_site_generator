import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()