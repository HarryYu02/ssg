import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_simple_paragraph(self):
        md = """
This is **bolded** and _italic_ paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> and <i>italic</i> paragraph</p></div>",
        )

    def test_simple_heading(self):
        md = """
## This is **bolded** and _italic_ h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>This is <b>bolded</b> and <i>italic</i> h2</h2></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """
- One
- Two
- Three
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>One</li><li>Two</li><li>Three</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. One
2. Two
3. Three
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>One</li><li>Two</li><li>Three</li></ol></div>",
        )

if __name__ == "__main__":
    unittest.main()
