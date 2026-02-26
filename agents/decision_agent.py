def parse_required_skills(skills_text):
    """
    Convert skills string from CSV into a clean list
    """
    if not skills_text:
        return []

    skills_text = skills_text.lower()
    skills = skills_text.replace("[", "").replace("]", "").replace("'", "")
    return [s.strip() for s in skills.split(",") if s.strip()]


def decision_agent(resume_skills, top_job_row):
    """
    Decide whether candidate should apply or improve resume
    """
    job_title = top_job_row["job_title"]
    category = top_job_row["category"]

    required_skills = parse_required_skills(top_job_row["required_skills"])

    resume_skills_set = set(resume_skills)
    required_skills_set = set(required_skills)

    matched_skills = resume_skills_set & required_skills_set
    missing_skills = required_skills_set - resume_skills_set

    match_ratio = (
        len(matched_skills) / len(required_skills_set)
        if required_skills_set else 0
    )

    if match_ratio >= 0.6:
        decision = "APPLY"
        reason = "Your profile matches most of the required skills."
    else:
        decision = "IMPROVE"
        reason = "You are missing several key skills for this role."

    return {
        "job_title": job_title,
        "category": category,
        "decision": decision,
        "match_ratio": round(match_ratio, 2),
        "matched_skills": sorted(list(matched_skills)),
        "missing_skills": sorted(list(missing_skills)),
        "reason": reason
    }
