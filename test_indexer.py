from app.loaders.pdf_loader import PDFLoader
from app.indexing.indexer import Indexer

loader = PDFLoader()

document = loader.load(
    r"C:\AIProjects\Repositories\Enterprise-AI-Knowledge-Hub\documents\sample.pdf"
)

indexer = Indexer()

indexer.index_document(document)