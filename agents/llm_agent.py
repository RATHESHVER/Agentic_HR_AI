import subprocess

def chat_with_llama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=120
        )
        return result.stdout.strip()
    except Exception as e:
        return f"LLaMA Error: {e}"


def rag_chat(user_query, job_context, resume_context):
    prompt = f"""
You are an AI HR assistant.

Job knowledge base (retrieved):
{job_context}

Resume screening context:
{resume_context}

User question:
{user_query}

Answer clearly, practically, and only using the given context.
"""
    return chat_with_llama(prompt)
