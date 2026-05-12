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

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return found_skills