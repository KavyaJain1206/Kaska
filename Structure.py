import os
import yaml

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    """Create file with optional content"""
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created file: {path}")

def setup_project():
    # Project root directory
    root = "project-root"
    create_directory(root)

    # Data directories
    data_dirs = [
        "data/raw",
        "data/processed",
        "data/output"
    ]
    for dir_path in data_dirs:
        create_directory(os.path.join(root, dir_path))

    # Modules directory and files
    modules_dir = os.path.join(root, "modules")
    create_directory(modules_dir)
    module_files = [
        "__init__.py",
        "preprocessing.py",
        "ocr_engine.py",
        "diagram_extractor.py",
        "markdown_generator.py",
        "exporter.py",
        "utils.py"
    ]
    for file in module_files:
        create_file(os.path.join(modules_dir, file))

    # API directory and files
    api_dir = os.path.join(root, "api")
    create_directory(api_dir)
    api_files = [
        "__init__.py",
        "app.py"
    ]
    for file in api_files:
        create_file(os.path.join(api_dir, file))

    # Tests directory and files
    tests_dir = os.path.join(root, "tests")
    create_directory(tests_dir)
    test_files = [
        "test_preprocessing.py",
        "test_ocr_engine.py",
        "test_markdown_generator.py",
        "test_exporter.py"
    ]
    for file in test_files:
        create_file(os.path.join(tests_dir, file))

    # Root level files
    root_files = {
        "requirements.txt": "",
        "Dockerfile": "FROM python:3.9-slim\n\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\n\nCMD [\"python\", \"main.py\"]",
        "docker-compose.yml": "version: '3'\nservices:\n  app:\n    build: .\n    volumes:\n      - ./data:/app/data",
        "main.py": "def main():\n    pass\n\nif __name__ == '__main__':\n    main()",
        "config.yaml": "pipeline:\n  preprocessing:\n    enabled: true\n  ocr:\n    enabled: true\n  export:\n    format: markdown",
        "README.md": "# Project Name\n\nDescription of your project goes here."
    }
    
    for filename, content in root_files.items():
        create_file(os.path.join(root, filename), content)

if __name__ == "__main__":
    setup_project()