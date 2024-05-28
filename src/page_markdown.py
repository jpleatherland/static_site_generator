import os
import shutil

from markdown_block import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return markdown_to_html_node(line).to_html()
    raise Exception("Page must contain a single h1 header")


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")

    target_path = "/".join(dest_path.split("/")[:-1])
    # copy template file to dest_path
    if not os.path.exists(target_path):
        os.mkdir()

    shutil.copy(template_path, dest_path)

    markdown_contents = ""

    with open(from_path) as markdown_file:
        markdown_contents = markdown_file.read()

    title = extract_title(markdown_contents)
    content = markdown_to_html_node(markdown_contents).to_html()

    template_contents = ""
    with open(dest_path) as template_file:
        template_contents = template_file.read()

    populated_template = template_contents.replace("{{ Title }}", title)
    populated_template = populated_template.replace("{{ Content }}", content)
    with open(dest_path, 'w') as target_file:
        target_file.write(populated_template)
