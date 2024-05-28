import os
import shutil

from markdown_block import markdown_to_html_node
from utils import path_join


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("Page must contain a single h1 header")


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")

    target_path = "/".join(dest_path.split("/")[:-1])
    # copy template file to dest_path
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    markdown_contents = ""

    with open(from_path) as markdown_file:
        markdown_contents = markdown_file.read()

    title = extract_title(markdown_contents)
    content = markdown_to_html_node(markdown_contents)

    template_contents = ""
    with open(template_path) as template_file:
        template_contents = template_file.read()

    populated_template = template_contents.replace(" {{ Title }} ", title)
    populated_template = populated_template.replace("{{ Content }}", content)

    with open(dest_path, 'w') as target_file:
        target_file.write(populated_template)


def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        fq_path = path_join(dir_path_content, item)
        target_path = path_join(dest_dir_path, item)
        if not os.path.isfile(fq_path):
            generate_pages_recursively(
                fq_path, template_path, target_path)
        elif item.endswith(".md"):
            target_path = target_path.split(".")
            target_path[-1] = "html"
            target_path = ".".join(target_path)
            generate_page(fq_path, template_path, target_path)
