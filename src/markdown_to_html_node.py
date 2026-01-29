import math

from markdown_to_blocks import BlockType, markdown_to_blocks, block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode


def markdown_to_html_node(markdown):
    html_node = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = None
        match block_type:
            case BlockType.PARAGRAPH:
                parent = ParentNode("p", [])
                block_textnodes = text_to_textnodes(block.replace("\n", " "))
                for textnode in block_textnodes:
                    leafnode = text_node_to_html_node(textnode)
                    parent.children.append(leafnode)
                html_node.children.append(parent)
            case BlockType.HEADING:
                count = 0
                i = 0
                while block[i] == "#":
                    count += 1
                    i += 1
                parent = ParentNode(f"h{count}", [])
                block_textnodes = text_to_textnodes(block[count+1:])
                for textnode in block_textnodes:
                    leafnode = text_node_to_html_node(textnode)
                    parent.children.append(leafnode)
                html_node.children.append(parent)
            case BlockType.CODE:
                parent = ParentNode("pre", [ParentNode("code", [LeafNode(None, block[4:-3])])])
                html_node.children.append(parent)
            case BlockType.QUOTE:
                parent = ParentNode("q", [])
                block_textnodes = text_to_textnodes(block)
                for textnode in block_textnodes:
                    leafnode = text_node_to_html_node(textnode)
                    parent.children.append(leafnode)
                html_node.children.append(parent)
            case BlockType.UNORDERED_LIST:
                parent = ParentNode("ul", [])
                lines = block.split("\n")
                for line in lines:
                    parent.children.append(LeafNode("li", line[2:]))
                html_node.children.append(parent)
            case BlockType.ORDERED_LIST:
                parent = ParentNode("ol", [])
                lines = block.split("\n")
                for line_num in range(1, len(lines)+1):
                    parent.children.append(LeafNode("li", lines[line_num-1][math.floor(math.log10(abs(line_num)))+3:]))
                html_node.children.append(parent)
            case _:
                raise Exception("Error: unkown block type")
    return html_node
