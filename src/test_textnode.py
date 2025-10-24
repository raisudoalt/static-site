import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_equal_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is not text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_equal_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_all_properties_equal(self):
        node1 = TextNode("Hello World", TextType.LINK, "https://example.com")
        node2 = TextNode("Hello World", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()