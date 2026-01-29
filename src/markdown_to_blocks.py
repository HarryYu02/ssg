def markdown_to_blocks(markdown):
    blocks = []

    splitted_markdown = markdown.split("\n\n")
    for block in splitted_markdown:
        formatted_block = block.strip()
        if len(formatted_block) > 0:
            blocks.append(formatted_block)

    return blocks
