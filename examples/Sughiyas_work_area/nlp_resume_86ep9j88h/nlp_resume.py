import spacy
from pdfminer.high_level import extract_text

# Load English language model for spaCy
nlp = spacy.load("en_core_web_sm")


def extract_skills_from_resume(resume_text):
    # Process text with spaCy
    doc = nlp(resume_text)

    # Define keywords indicating skills
    skill_keywords = ["python", "java", "c++", "communication", "html", "css", "teamwork", "problem-solving", "javascript"]
    lowercase_words = [keyword.lower() for keyword in skill_keywords]

    # Extract skills based on keywords
    skills = []
    for token in doc:
        if token.text.lower() in lowercase_words:
            skills.append(token.text)

    return skills


def main():
    # Path to the resume PDF file
    resume_path = "./entry.pdf"  # Replace with your resume path

    # Extract text from PDF
    resume_text = extract_text(resume_path)

    # Extract skills from resume text
    extracted_skills = extract_skills_from_resume(resume_text)

    # Remove duplicate skills
    unique_skills = list(set(extracted_skills))

    # Print extracted skills
    print("Extracted Skills:")
    for skill in unique_skills:
        print(skill)


if __name__ == "__main__":
    main()
