import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_jobs(resume_text, top_n=3, preferred_category=None):
    # Load jobs dataset
    jobs = pd.read_csv("data/jobs.csv")

    # Optional category filtering (agentic behavior)
    if preferred_category:
        jobs = jobs[jobs["category"].str.lower() == preferred_category.lower()]

    # Combine resume with job descriptions
    corpus = [resume_text] + jobs["job_description"].tolist()

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(corpus)

    # Similarity between resume and each job
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:])[0]

    jobs = jobs.copy()
    jobs["match_score"] = similarity_scores

    # Return top matching jobs
    top_jobs = jobs.sort_values(by="match_score", ascending=False).head(top_n)

    return top_jobs
