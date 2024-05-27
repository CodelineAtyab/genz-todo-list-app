import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load('en_core_web_sm')


def extract_skills(text):
    doc = nlp(text)
    skills = []
    for ent in doc.ents:
        if ent.label_ == 'SKILL':
            skills.append(ent.text)

    technical_skills_keywords = [
        "Visual Basic", "SQL", "C", "C++", "Java",
        "Windows NT", "Windows 2000", "Windows XP", "Windows Vista",
        "Linux", "Unix",
        "SQL Server", "MS Access", "Oracle",
        "JCL", "DB2", "MS Visio", "MS Excel", "MS FrontPage", "MS Word"
    ]
    for token in doc:
        if token.text in technical_skills_keywords and token.text not in skills:
            skills.append(token.text)

    return skills


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


resume_path = "CSExampleResume.pdf"
resume_text = extract_text_from_pdf(resume_path)
skills = extract_skills(resume_text)

print("Extracted Skills:", skills)


