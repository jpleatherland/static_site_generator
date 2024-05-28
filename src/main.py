import shutil
import os


from textnode import TextNode
from page_markdown import generate_pages_recursively
from utils import path_join

source_tree = "static"
dest_tree = "public"


def static_to_public(source_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path, ignore_errors=True)

    # specifically instructed not to use shutil.copytree
    recursive_copy(source_path, dest_path)


def recursive_copy(path, dest_path):
    target_path = path_join(dest_path, '/'.join(path.split("/")[1:]))
    for item in os.listdir(path):
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        fq_path = path_join(path, item)
        if os.path.isfile(fq_path):
            shutil.copy(fq_path, target_path)
        else:
            recursive_copy(path_join(path, item), dest_path)


def main():
    static_to_public(source_tree, dest_tree)
    generate_pages_recursively("content", "template.html", "public")


main()
