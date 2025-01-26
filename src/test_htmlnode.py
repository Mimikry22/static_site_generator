import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_parentnode_values(self):
        node = ParentNode("a", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("a", "Click me!", {"href": "https://www.google.com"})])
        self.assertEqual(node.to_html(), '<a><b>Bold text</b>Normal text<a href="https://www.google.com">Click me!</a></a>')

    def test_parentnode_no_children(self):
        node = ParentNode("a", None, {"href": "https://www.google.com"})
        
        with self.assertRaises(ValueError) as cm:
            node.to_html()
            self.assertTrue("Invalid HTML: no children" in cm.exception)
    
    def test_parentnode_no_tag(self):
        node = ParentNode(None, None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError) as cm:
            node.to_html()
            self.assertTrue("Invalid HTML: no tag" in cm.exception)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>", )

if __name__ == "__main__":
    unittest.main()