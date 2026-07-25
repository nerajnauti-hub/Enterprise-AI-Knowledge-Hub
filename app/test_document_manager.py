from app.document.document_manager import DocumentManager

manager = DocumentManager()

documents = manager.list_documents()

print()

print("=" * 60)
print("DOCUMENT LIBRARY")
print("=" * 60)

for index, doc in enumerate(documents, start=1):

    print(
        f"{index}. {doc['name']} "
        f"({doc['extension']}) "
        f"{doc['size']/1024:.1f} KB"
    )