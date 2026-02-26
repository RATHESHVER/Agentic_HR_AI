import pandas as pd

# Load original dataset (Windows local path)
df = pd.read_csv("all_job_post.csv")

# Keep required columns
df = df[["job_title", "job_description", "job_skill_set", "category"]]

# Rename column
df = df.rename(columns={
    "job_skill_set": "required_skills"
})

# Drop missing values
df.dropna(inplace=True)

# Ensure skills are string
df["required_skills"] = df["required_skills"].astype(str)

# Save cleaned file into data folder
df.to_csv("data/jobs.csv", index=False)

print("✅ jobs.csv created successfully inside data folder!")
print(df.head())
