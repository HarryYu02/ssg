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
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        text = old_node.text[:]
        for image in images:
            alt = image[0]
            url = image[1]
            idx = text.index(f"![{alt}]({url})")
            if idx > 0:
                new_nodes.append(TextNode(text[:idx], TextType.PLAIN))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = text[idx+len(alt)+len(url)+5:]

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        text = old_node.text[:]
        for link in links:
            link_text = link[0]
            url = link[1]
            idx = text.index(f"[{link_text}]({url})")
            if idx > 0:
                new_nodes.append(TextNode(text[:idx], TextType.PLAIN))
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            text = text[idx+len(link_text)+len(url)+4:]

    return new_nodes

