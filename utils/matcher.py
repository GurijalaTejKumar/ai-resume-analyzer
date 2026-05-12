from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS_DB = [
    "python",
    "sql",
    "fastapi",
    "machine learning",
    "tensorflow",
    "keras",
    "opencv",
    "aws",
    "git",
    "github",
    "docker",
    "linux",
    "api",
    "pandas",
    "numpy"
]

def calculate_match(resume_text, job_description):

    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer().fit_transform(documents)

    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])

    score = round(float(similarity[0][0]) * 100, 2)

    return score


def missing_skills(resume_skills, job_description):

    job_description = job_description.lower()

    missing = []

    for skill in SKILLS_DB:

        if skill in job_description and skill not in resume_skills:
            missing.append(skill)

    return missing