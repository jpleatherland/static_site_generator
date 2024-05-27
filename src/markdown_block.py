block_types = {
    "block_type_paragraph" : "paragraph",
    "block_type_h1" : "h1",
    "block_type_h2" : "h2",
    "block_type_h3" : "h3",
    "block_type_h4" : "h4",
    "block_type_h5" : "h5",
    "block_type_h6" : "h6",
    "block_type_code" : "code",
    "block_type_quote" : "quote",
    "block_type_ul" : "unordered_list",
    "block_type_ol" : "ordered_list"
}

def markdown_to_blocks(markdown):
    blocks = []
    for line in markdown.split("\n\n"):
        line = line.strip()
        if len(line) > 0:
            blocks.append(line)
    return blocks

def block_to_block_type(block):
    if block.startswith("# "):
        return block_types['block_type_h1']
    if block.startswith("## "):
        return block_types['block_type_h2']
    if block.startswith("### "):
        return block_types['block_type_h3']
    if block.startswith("#### "):
        return block_types['block_type_h4']
    if block.startswith("##### "):
        return block_types['block_type_h5']
    if block.startswith("###### "):
        return block_types['block_type_h6']
    if block.startswith("```") and block.endswith("```"):
        return block_types['block_type_code']
    if block.startswith("> "):
        return block_types['block_type_quote']
    if block.startswith("- ") or block.startswith("* "):
        return block_types['block_type_ul']
    if block.startswith("1. "):
        for i in range(0, len(block.split("\n"))):
            if not block.split("\n")[i].strip().startswith(f"{i+1}."):
                return block_types['block_type_paragraph']
        return block_types['block_type_ol']
    return block_types['block_type_paragraph']