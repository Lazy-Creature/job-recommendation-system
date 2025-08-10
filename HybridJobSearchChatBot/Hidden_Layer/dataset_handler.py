import pandas as pd
import os

def load_dataset():
    data_path=os.path.join(os.path.dirname(__file__), "..", "data", "jobs.csv")
    df=pd.read_csv("data/jobs.csv", quotechar='"')
    return df

def find_relevant_jobs(resume_text, df, top_n=3):
    """
    Very simple skill-based matching from resume_text.
    You can improve with embeddings for better accuracy.
    """
    matches=[]
    resume_lower=resume_text.lower()
    for _, row in df.iterrows():
        skills=[s.strip().lower() for s in str(row["skills"]).split(",")]
        score=sum(1 for skill in skills if skill in resume_lower)
        matches.append((score, row["title"], row["company"], row["location"], row["skills"], row["experience"], row["description"]))

    # Sort by score and return top_n
    matches=sorted(matches, key=lambda x: x[0], reverse=True)
    return [m for m in matches if m[0] > 0][:top_n]

#