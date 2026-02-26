# agents/skill_extractor.py

SKILLS_DB = [
    "python",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "data science",
    "sql",
    "flask",
    "django",
    "tensorflow",
    "pytorch",
    "scikit learn",
    "html",
    "css",
    "javascript",
    "react",
    "fullstack",
    "api",
    "git",
    "github"
]

def extract_skills(resume_text):
    found_skills = set()

    for skill in SKILLS_DB:
        if skill in resume_text:
            found_skills.add(skill)

    return sorted(list(found_skills))
