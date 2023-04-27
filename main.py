import os
import sys
import pypdf
import logging
from dataclasses import dataclass


def log_config():
    """Performs a logging basic setup"""
    handler_to_file = logging.FileHandler("log.log", "w")
    handler_to_file.setLevel(logging.DEBUG)
    handler_to_console = logging.StreamHandler()
    handler_to_console.setLevel(logging.ERROR)
    logging.basicConfig(
        handlers=[
            handler_to_file,
            handler_to_console,
        ],
        format="%(asctime)s: %(levelname)s %(filename)s %(lineno)s: %(message)s",
        level=logging.DEBUG,
    )


def get_base_dir():
    """Get base dir, regardless if running from script or frozen exe"""
    # https://stackoverflow.com/questions/404744/determining-application-path-in-a-python-exe-generated-by-pyinstaller
    if getattr(sys, "frozen", False):
        logging.debug("Running from executable file")
        return os.path.dirname(sys.executable)
    else:
        logging.debug("Running from script")
        return os.path.dirname(os.path.realpath(__file__))


@dataclass
class Document:
    "Class representing any file to scan"
    path: str


@dataclass
class PdfDoc(Document):
    "Class representing Pdf file to scan"

    # https://stackoverflow.com/questions/51199031/python-3-dataclass-initialization
    def __post_init__(self):
        self.reader = pypdf.PdfReader(self.path)
        self.texts = []
        for page in self.reader.pages:
            this_text = page.extract_text()
            self.texts.append(this_text)


@dataclass
class DocMgr:
    base_dir: str

    def import_docs(self):
        """Imports documents from input dir"""
        self.pdfs = []
        self.words = []
        input_dir = os.path.join(self.base_dir, "input")
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith(".pdf"):
                    self.pdfs.append(PdfDoc(file_path))
                elif file.endswith(".docx"):
                    pass
                else:
                    logging.error("Document with unexpected format: %s", file_path)

    def filter_docs(self):
        """Copies the docs that pass the filter into a new folder"""


if __name__ == "__main__":
    log_config()
    logging.debug("Program started")
    base_dir = get_base_dir()
    logging.debug("Main folder found at %s", base_dir)
    doc_mgr = DocMgr(base_dir)
    print(doc_mgr.base_dir)
    doc_mgr.import_docs()
    doc_mgr.filter_docs()
