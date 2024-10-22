import os

def get_file_comment(filepath):
    """Extract the first docstring (triple quotes) from a Python file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        triple_quote_start = content.find('"""')  # Look for the opening triple quotes
        if triple_quote_start == -1:
            triple_quote_start = content.find("'''")  # Try single quotes

        if triple_quote_start != -1:
            triple_quote_end = content.find('"""', triple_quote_start + 3)
            if triple_quote_end == -1:
                triple_quote_end = content.find("'''", triple_quote_start + 3)

            if triple_quote_end != -1:
                docstring = content[triple_quote_start + 3:triple_quote_end].strip()
                return docstring

    return None


def create_index(root_folder):
    index_content = "# Index of Python Exercises\n\n"

    # Get all subdirectories and sort them
    subdirs = [d for d in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, d))]
    subdirs.sort()

    # Process each subdirectory
    for subdir_name in subdirs:
        subdir_path = os.path.join(root_folder, subdir_name)
        relative_subdir = os.path.relpath(subdir_path, root_folder)
        index_content += f"## [{relative_subdir}]({relative_subdir})\n\n"

        # Get all Python files in the current subdirectory and sort them
        files = [f for f in os.listdir(subdir_path) if f.endswith(".py")]
        sorted_files = sorted(files)

        for file in sorted_files:
            filepath = os.path.join(subdir_path, file)
            relative_path = os.path.relpath(filepath, root_folder)

            # Get the comment (docstring) from the file
            comment = get_file_comment(filepath)
            if comment:
                # Format the comment in a Python code block without any '>'
                comment_text = f"\n```text\n{comment}\n```\n"
            else:
                comment_text = ""  # No comment (docstring) available

            # Create a clickable link with formatted docstring
            index_content += f"- [{file}]({relative_path})\n{comment_text}"

        index_content += "\n---\n"  # Add a separator between folders

    # Write the index to `index_ex.md`
    with open(os.path.join(root_folder, 'index_ex.md'), 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)

# Specify the root folder
project_folder = os.path.dirname(os.path.abspath(__file__))  # Adjust as necessary

# Create the index
create_index(project_folder)
