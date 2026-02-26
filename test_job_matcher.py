from agents.resume_parser import parse_resume
from agents.job_matcher import match_jobs

resume_text = parse_resume("sample_resume.pdf")

matched_jobs = match_jobs(resume_text, top_n=3)

print("✅ Top Matching Jobs:\n")
for _, row in matched_jobs.iterrows():
    print("Job Title:", row["job_title"])
    print("Category:", row["category"])
    print("Match Score:", round(row["match_score"], 3))
    print("-" * 40)
