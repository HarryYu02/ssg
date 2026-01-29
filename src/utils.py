import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type not in [TextType.BOLD, TextType.ITALIC, TextType.CODE]:
        raise Exception("Error: invalid text_type")

    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        splitted = old_node.text.split(delimiter)
        if len(splitted) < 3 or len(splitted) % 2 == 0:
            raise Exception("Error: node not properly enclosed")

        for i in range(0, len(splitted)):
            if len(splitted[i]) == 0:
                continue
            new_node = TextNode(splitted[i], text_type if i % 2 == 1 else TextType.PLAIN)
            new_nodes.append(new_node)

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"\!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!\!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    pass

