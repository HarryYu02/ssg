import unittest

from markdown_to_blocks import markdown_to_blocks, BlockType, block_to_block_type


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line






- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        h1 = "# heading 1"
        h2 = "## heading 2"
        h3 = "### heading 3"
        h4 = "#### heading 4"
        h5 = "##### heading 5"
        h6 = "###### heading 6"
        self.assertEqual(block_to_block_type(h1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(h2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(h3), BlockType.HEADING)
        self.assertEqual(block_to_block_type(h4), BlockType.HEADING)
        self.assertEqual(block_to_block_type(h5), BlockType.HEADING)
        self.assertEqual(block_to_block_type(h6), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        code = "```\nprint('hello, world!')\nreturn 0\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        quote = ">To be or not to be, that's the question"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_block_to_block_type_ul(self):
        ul = "- first\n- second\n- third"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ol(self):
        ol = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        paragraph = "This is a paragraph"
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
