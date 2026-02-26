from agents.resume_parser import parse_resume
from agents.skill_extractor import extract_skills

resume_text = parse_resume("sample_resume.pdf")
skills = extract_skills(resume_text)

print("✅ Extracted Skills:")
print(skills)
