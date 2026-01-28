import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_with_attr(self):
        node = LeafNode("p", "Hello, world!", { "class": "text" })
        self.assertEqual(node.to_html(), '<p class="text">Hello, world!</p>')

    def test_leaf_to_html_p_with_attrs(self):
        node = LeafNode("p", "Hello, world!", { "class": "text", "foo": "bar", "lorem": "" })
        self.assertEqual(node.to_html(), '<p class="text" foo="bar" lorem="">Hello, world!</p>')


if __name__ == "__main__":
    unittest.main()
