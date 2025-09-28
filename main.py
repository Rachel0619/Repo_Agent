from src.chunking import split_markdown_by_level
from src.read_repo import read_repo_data
from src.search import text_search, vector_search, hybrid_search

if __name__ == "__main__":
    owner = 'rachel0619'
    repo = 'VanTrails'
    data = read_repo_data(owner, repo)

    chunks = []

    for doc in data:
        doc_copy = doc.copy()
        doc_content = doc_copy.pop('content')
        sections = split_markdown_by_level(doc_content, level=2)
        for section in sections:
            section_doc = doc_copy.copy()
            section_doc['section'] = section
            chunks.append(section_doc)

    query = "what tech stack does VanTrails use?"

    # result = text_search(chunks, query)
    result = vector_search(chunks, query)
    # result = hybrid_search(chunks, query)
