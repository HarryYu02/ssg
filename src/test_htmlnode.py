import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "hello, world!", None, { "class": "text" })
        expected = "HTML Node:\nTag: p\nValue: hello, world!\nChildren: None\nProps: {'class': 'text'}"
        self.assertEqual(str(node), expected)

    def test_props_html(self):
        node = HTMLNode("a", "hello, world!", None, {
            "class": "link",
            "href": "https://www.google.com",
            "target": "_blank",
        })
        expected = ' class="link" href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_html(), expected)


if __name__ == "__main__":
    unittest.main()
