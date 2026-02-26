from agents.resume_parser import parse_resume
from agents.skill_extractor import extract_skills
from agents.job_matcher import match_jobs
from agents.decision_agent import decision_agent

# Step 1: Parse resume
resume_text = parse_resume("sample_resume.pdf")

# Step 2: Extract skills
resume_skills = extract_skills(resume_text)

# Step 3: Match jobs
top_jobs = match_jobs(resume_text, top_n=1)

top_job = top_jobs.iloc[0]

# Step 4: Decision making
decision = decision_agent(resume_skills, top_job)

print("\n🧠 FINAL DECISION\n")
for key, value in decision.items():
    print(f"{key}: {value}")
