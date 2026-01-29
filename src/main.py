import os
import shutil


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


def main():
    copy_tree("static", "public")

if __name__ == "__main__":
    main()
