import os
import shutil
import sys

from markdown_to_html_node import markdown_to_html_node


def copy_tree(src, dest):
    abs_src = os.path.abspath(src)
    abs_dest = os.path.abspath(dest)
    if not os.path.exists(abs_src) or not os.path.exists(abs_dest):
        raise Exception("Error: src or dest not found")
    if not os.path.isdir(abs_src) or not os.path.isdir(abs_dest):
        raise Exception("Error: src or dest not a directory")

    shutil.rmtree(abs_dest)
    os.mkdir(abs_dest)

    src_contents = os.listdir(abs_src)
    for content in src_contents:
        abs_content_path = os.path.join(abs_src, content)
        if os.path.isfile(abs_content_path):
            shutil.copy(abs_content_path, abs_dest)
        elif os.path.isdir(abs_content_path):
            abs_content_dest_path = os.path.join(abs_dest, content)
            os.mkdir(abs_content_dest_path)
            copy_tree(abs_content_path, abs_content_dest_path)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("Error: markdown has no h1 header")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as from_file:
        markdown = from_file.read()
        with open(template_path, "r") as template_file:
            template = template_file.read()
            htmlnode = markdown_to_html_node(markdown)
            html_content = htmlnode.to_html()
            title = extract_title(markdown)
            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html_content)
            template = template.replace('href="', f'href="{basepath}')
            template = template.replace('src="', f'src="{basepath}')

            dest_dir = os.path.dirname(dest_path)
            if not os.path.exists(dest_path):
                os.makedirs(dest_dir, exist_ok=True)
                with open(dest_path, "w") as dest_file:
                    dest_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    contents = os.listdir(dir_path_content)
    for content in contents:
        content_path = os.path.join(dir_path_content, content)
        if os.path.isfile(content_path) and content.endswith(".md"):
            dest = os.path.join(dest_dir_path, content)
            dest = dest.replace(".md", ".html")
            generate_page(content_path, template_path, dest, basepath)
        elif os.path.isdir(content_path):
            generate_pages_recursive(content_path, template_path, os.path.join(dest_dir_path, content), basepath)


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_tree("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
