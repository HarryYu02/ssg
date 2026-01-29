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
        new_splitted_nodes = []
        for i in range(0, len(splitted)):
            splitted_text = splitted[i]
            if len(splitted_text) == 0:
                continue
            if i % 2 == 0:
                new_splitted_nodes.append(TextNode(splitted_text, TextType.PLAIN))
            else:
                new_splitted_nodes.append(TextNode(splitted_text, text_type))
        new_nodes.extend(new_splitted_nodes)

    return new_nodes
