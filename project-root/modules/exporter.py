from modules.markdown_generator import generate_markdown
from fpdf import FPDF

def export_to_txt(text, output_path):
    """Export extracted text to a .txt file"""
    with open(output_path, 'w') as file:
        file.write(text)

def export_to_md(text, output_path):
    """Export extracted text to a .md (Markdown) file"""
    markdown_text = generate_markdown(text)
    with open(output_path, 'w') as file:
        file.write(markdown_text)

def export_to_pdf(text, output_path):
    """Export extracted text to a .pdf file"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)  # Adds the text to the PDF file
    pdf.output(output_path)

def export_text(image_text, format='txt', output_path="output/extracted_text"):
    """Export extracted text to the desired format"""
    if format == 'txt':
        export_to_txt(image_text, f"{output_path}.txt")
    elif format == 'md':
        export_to_md(image_text, f"{output_path}.md")
    elif format == 'pdf':
        export_to_pdf(image_text, f"{output_path}.pdf")
    else:
        print("Invalid format. Please choose 'txt', 'md', or 'pdf'.")
