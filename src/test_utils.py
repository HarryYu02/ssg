import unittest

from utils import split_nodes_delimiter
from textnode import TextNode, TextType


class TestUtils(unittest.TestCase):
    def test_non_plain(self):
        bold_node = TextNode("This is text with a `code block` word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([bold_node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [bold_node])

    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.PLAIN),
        ])

    def test_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.PLAIN),
        ])

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ])

    def test_code_start(self):
        node = TextNode("`code block` is in the start.", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("code block", TextType.CODE),
            TextNode(" is in the start.", TextType.PLAIN),
        ])

    def test_code_end(self):
        node = TextNode("The code is in the end: `code block`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("The code is in the end: ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
        ])

    def test_code_only(self):
        node = TextNode("`code block`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("code block", TextType.CODE),
        ])

    def test_two_code(self):
        node = TextNode("This have `code block` and `code block` in the text", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This have ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" in the text", TextType.PLAIN),
        ])

if __name__ == "__main__":
    unittest.main()
