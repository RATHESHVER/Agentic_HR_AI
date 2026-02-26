print("🔥 test_resume_parser.py is running")

from agents.resume_parser import parse_resume

print("🔥 Imported parse_resume successfully")

resume_text = parse_resume("sample_resume.pdf")

print("🔥 Resume parsed successfully")
print("First 300 characters:")
print(resume_text[:300])
