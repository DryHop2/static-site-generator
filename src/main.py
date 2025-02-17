import os
import shutil
from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# dir_path_static = "./static"
# dir_path_public = "./public"
dir_path_static = os.path.join(BASE_DIR, "static")
dir_path_public = os.path.join(BASE_DIR, "public")
content_path = os.path.join(BASE_DIR, "content")
template_path = os.path.join(BASE_DIR, "template.html")
# output_path = os.path.join(BASE_DIR, "public", "index.html")


def main():
    print("Starting site generation...")

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Calling generate_page...")
    generate_pages_recursive(content_path, template_path, dir_path_public)

    print("Site generation complete.")


main()