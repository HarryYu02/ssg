import math

from markdown_to_blocks import BlockType, markdown_to_blocks, block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode


def get_num_digits(num):
    return math.floor(math.log10(abs(num)))+1

def count_prefix_char(prefix, s):
    count = 0
    i = 0
    while s[i] == prefix:
        count += 1
        i += 1
    return count

def transform_text_and_append_to_parent_node(text, parent):
    block_textnodes = text_to_textnodes(text)
    for textnode in block_textnodes:
        leafnode = text_node_to_html_node(textnode)
        parent.children.append(leafnode)

def markdown_to_html_node(markdown):
    html_node = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = None
        match block_type:
            case BlockType.PARAGRAPH:
                block_node = ParentNode("p", [])
                transform_text_and_append_to_parent_node(block.replace("\n", " "), block_node)
            case BlockType.HEADING:
                count = count_prefix_char("#", block)
                block_node = ParentNode(f"h{count}", [])
                transform_text_and_append_to_parent_node(block[count+1:], block_node)
            case BlockType.CODE:
                block_node = ParentNode("pre", [ParentNode("code", [LeafNode(None, block[4:-3])])])
            case BlockType.QUOTE:
                block_node = ParentNode("blockquote", [])
                quote = ""
                lines = block.split("\n")
                for line in lines:
                    if line.startswith("> "):
                        quote += line[2:]
                    elif line.startswith(">"):
                        quote += line[1:]
                    quote += "\n"
                transform_text_and_append_to_parent_node(quote, block_node)
            case BlockType.UNORDERED_LIST:
                block_node = ParentNode("ul", [])
                lines = block.split("\n")
                for line in lines:
                    list_item = ParentNode("li", [])
                    transform_text_and_append_to_parent_node(line[2:], list_item)
                    block_node.children.append(list_item)
            case BlockType.ORDERED_LIST:
                block_node = ParentNode("ol", [])
                lines = block.split("\n")
                for line_num in range(1, len(lines)+1):
                    list_item = ParentNode("li", [])
                    transform_text_and_append_to_parent_node(lines[line_num-1][get_num_digits(line_num)+2:], list_item)
                    block_node.children.append(list_item)
            case _:
                raise Exception("Error: unkown block type")
        if block_node:
            html_node.children.append(block_node)
    return html_node
