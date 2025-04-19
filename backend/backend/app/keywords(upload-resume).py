import fitz  # PyMuPDF for PDFs
import docx
import json
from paddleocr import PaddleOCR
from google.colab import files
import google.generativeai as genai

def upload_resume():
    uploaded = files.upload()
    for filename in uploaded.keys():
        return filename  # Return the uploaded file path
    return None

def extract_text_from_resume(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
        return text

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        ocr = PaddleOCR()
        result = ocr.ocr(file_path, cls=True)
        extracted_text = " ".join([line[1][0] for line in result[0] if line[1]])
        return extracted_text

    else:
        return "Unsupported file format. Please upload a PDF, DOCX, or image."

def extract_resume_details(api_key, resume_text):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = (
        "Analyze the given resume text and extract information dynamically. "
        "Use the headings present in the resume as JSON keys, and structure the content under each heading as appropriate subfields. "
        "If a section contains multiple entries (e.g., Education, Certifications, Projects, etc.), format them as a list of structured objects. "
        "Ensure the output is properly formatted, with each section preserving its hierarchical structure without adding predefined fields. "
        "Detect and extract personal details such as Name, Email, LinkedIn, and Phone if present. "
        "Additionally, combine all technical stacks from different sections (Skills, Areas of Interest, etc.) into a single 'Skills' key. "
        "Ensure that no subcategories are included in 'Skills'—only a flat list of all technical skills.\n\n"
        f"Resume Text:\n{resume_text}\n\n"
    )

    response = model.generate_content(prompt)
    try:
        extracted_data = json.loads(response.text)
        return extracted_data
    except json.JSONDecodeError:
        return response.text

api_key = "apikey"
print("Please upload your resume (PDF, DOCX, or Image):")
resume_file = upload_resume()
resume_text = extract_text_from_resume(resume_file)
resume_details = extract_resume_details(api_key, resume_text)

print("Extracted Resume Details:", resume_details)