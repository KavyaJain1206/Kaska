def generate_markdown(text):
    """Convert extracted text into Markdown format"""
    lines = text.split('\n')
    markdown_text = ""

    for line in lines:
        if line.startswith('Q:'):
            markdown_text += f"## {line[2:]}\n"  # Question as header
        else:
            markdown_text += f"{line}\n"  # Answer as paragraph

    return markdown_text
