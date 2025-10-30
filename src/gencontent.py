import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for name in os.listdir(dir_path_content):
        if name.startswith("."):
            continue  # skip hidden files/dirs like .DS_Store

        from_path = os.path.join(dir_path_content, name)
        dest_path = os.path.join(dest_dir_path, name)

        if os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, dest_path)
            continue

        if not name.endswith(".md"):
            continue  # only process markdown

        # map foo/index.md -> foo/index.html (same relative structure)
        if name == "index.md":
            out_path = os.path.join(dest_dir_path, "index.html")
        else:
            out_path = str(Path(dest_path).with_suffix(".html"))

        generate_page(from_path, template_path, out_path)


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
