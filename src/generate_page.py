import os
from inline_markdown import extract_title
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.exists(from_path):
        raise FileNotFoundError(f"Markdown file not found: {from_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Page generated successfully: {dest_path}")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Starting recursive page generation from {dir_path_content}...")

    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                generate_page(from_path, template_path, dest_path)

    print("Recursive page generation complete.")