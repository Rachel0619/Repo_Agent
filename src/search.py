from minsearch import VectorSearch
from sentence_transformers import SentenceTransformer
from minsearch import Index
from tqdm.auto import tqdm
import numpy as np

def text_search(texts, query):
    faq_index = Index(
        text_fields=["filename", "section"],
        keyword_fields=[]
    )
    faq_index.fit(texts)
    return faq_index.search(query, num_results=5)

def vector_search(texts, query):

    embeddings = []
    embedding_model = SentenceTransformer('multi-qa-distilbert-cos-v1')
    for d in tqdm(texts):
        v = embedding_model.encode(d['section'])
        embeddings.append(v)
    embeddings = np.array(embeddings)
    repo_vindex = VectorSearch()
    repo_vindex.fit(embeddings, texts)
    q = embedding_model.encode(query)
    return repo_vindex.search(q, num_results=5)

def hybrid_search(texts, query):
    text_results = text_search(texts, query)
    vector_results = vector_search(texts, query)
    
    # Combine and deduplicate results
    seen_ids = set()
    combined_results = []

    for result in text_results + vector_results:
        if result['filename'] not in seen_ids:
            seen_ids.add(result['filename'])
            combined_results.append(result)
    
    return combined_results