import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

faiss_index = None
job_texts = None


def build_job_kb(csv_path="data/jobs.csv"):
    global faiss_index, job_texts

    df = pd.read_csv(csv_path)

    job_texts = (
        df["job_title"] + ". " +
        df["job_description"] + ". Required skills: " +
        df["required_skills"]
    ).tolist()

    embeddings = model.encode(job_texts)
    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dim)
    faiss_index.add(embeddings)


def retrieve_job_context(query, top_k=3):
    query_embedding = model.encode([query]).astype("float32")
    _, indices = faiss_index.search(query_embedding, top_k)

    return "\n\n".join([job_texts[i] for i in indices[0]])
