from flask import Flask, render_template, request
import os

# -------- Core Agents --------
from agents.resume_parser import parse_resume
from agents.skill_extractor import extract_skills
from agents.job_matcher import match_jobs
from agents.decision_agent import decision_agent

# -------- RAG + LLM Agents --------
from agents.rag_agent import build_job_kb, retrieve_job_context
from agents.llm_agent import rag_chat

# -------- Flask App --------
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Build FAISS Job Knowledge Base ONCE at startup
build_job_kb()


# =====================================
# Resume Upload & Screening
# =====================================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]

        if not file:
            return "No file uploaded"

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # ----- Agent Pipeline -----
        resume_text = parse_resume(file_path)
        resume_skills = extract_skills(resume_text)

        top_jobs = match_jobs(resume_text, top_n=1)
        top_job = top_jobs.iloc[0]

        decision = decision_agent(resume_skills, top_job)

        return render_template(
            "result.html",
            decision=decision,
            resume_skills=resume_skills
        )

    return render_template("index.html")


# =====================================
# CONTEXT-AWARE RAG CHAT (RESULT PAGE)
# =====================================
@app.route("/resume_chat", methods=["POST"])
def resume_chat():
    user_message = request.form.get("message")

    # Resume screening context (from hidden fields)
    job_title = request.form.get("job_title")
    decision = request.form.get("decision")
    match_ratio = request.form.get("match_ratio")
    matched_skills = request.form.get("matched_skills")
    missing_skills = request.form.get("missing_skills")

    # ----- Resume Context -----
    resume_context = f"""
Recommended Job: {job_title}
Decision: {decision}
Match Ratio: {match_ratio}
Matched Skills: {matched_skills}
Missing Skills: {missing_skills}
"""

    # ----- RAG: Retrieve job info from FAISS -----
    job_context = retrieve_job_context(user_message)

    # ----- LLaMA-3 with RAG -----
    response = rag_chat(
        user_query=user_message,
        job_context=job_context,
        resume_context=resume_context
    )

    return response


# =====================================
# Run App
# =====================================
if __name__ == "__main__":
    app.run(debug=True)
