from fastapi import FastAPI, UploadFile, File, Form
from utils.parser import extract_text
from utils.skills import extract_skills
from utils.matcher import calculate_match, missing_skills
from utils.recommend import generate_recommendations
import tempfile

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Resume Analyzer Running 🚀"}


@app.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_path = temp_file.name

    # Extract resume text
    extracted_text = extract_text(temp_path)

    # Extract skills from resume
    skills = extract_skills(extracted_text)

    # Calculate job match score
    match_score = calculate_match(
        extracted_text,
        job_description
    )

    # Detect missing skills
    missing = missing_skills(
        skills,
        job_description
    )

    # Generate recommendations
    recommendations = generate_recommendations(
        missing
    )

    # Final API response
    return {
        "filename": file.filename,
        "skills": skills,
        "missing_skills": missing,
        "recommendations": recommendations,
        "match_score": f"{match_score}%",
        "text_preview": extracted_text[:300]
    }