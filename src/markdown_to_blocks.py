from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []

    splitted_markdown = markdown.split("\n\n")
    for block in splitted_markdown:
        formatted_block = block.strip()
        if len(formatted_block) > 0:
            blocks.append(formatted_block)

    return blocks

def block_to_block_type(block):
    if re.search(r"^#{1,6} .*", block):
        return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    if block.startswith(">"):
        return BlockType.QUOTE

    lines = block.split("\n")
    if all(map(lambda line: line.startswith("- "), lines)):
        return BlockType.UNORDERED_LIST

    counter = 1
    def starts_with_counter(line):
        nonlocal counter
        result = line.startswith(f"{counter}. ")
        counter += 1
        return result
    if all(map(starts_with_counter, lines)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
