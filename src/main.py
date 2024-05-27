from textnode import TextNode
import shutil
import os


def static_to_public():
    if os.path.exists("public"):
        shutil.rmtree("public", ignore_errors=True)
    # specifically told to not to use shutil.copytree
    recursive_copy("static")


def next_path(current_path, next_dir):
    return os.path.join(current_path, next_dir)


def recursive_copy(path):
    target_path = next_path("public", '/'.join(path.split("/")[1:]))
    for item in os.listdir(path):
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        fq_path = next_path(path, item)
        if os.path.isfile(fq_path):
            shutil.copy(fq_path, target_path)
        else:
            recursive_copy(next_path(path, item))


def main():
    static_to_public()


main()
print("hello world")
