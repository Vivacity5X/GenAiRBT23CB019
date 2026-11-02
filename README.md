# 🎯 SmartHireAI — AI-Powered Resume Screening

SmartHireAI is an AI-powered resume screening application built using **Python, DSPy, Google's Gemini API, and Streamlit**. It analyzes candidate resumes, extracts technical skills, evaluates alignment with a job description, identifies missing or unverified skills, and generates interview questions.

The project combines a structured AI evaluation pipeline with an interactive web interface to simplify preliminary resume screening.

## ✨ Features

- **📄 Resume Upload:** Upload candidate resumes in PDF format.
- **🧠 Skill Extraction:** Identify technical skills and relevant experience from resumes.
- **💼 Job Matching:** Compare candidate qualifications against a provided job description.
- **📊 Suitability Scoring:** Generate an estimated job-match score from 0 to 100.
- **🔍 Skills Gap Analysis:** Identify matching, missing, and unverified skills.
- **💬 Interview Questions:** Generate questions to help verify candidate qualifications.
- **📋 Structured Reports:** Display candidate analysis and job-matching results.
- **⬇️ JSON Export:** Download the evaluation report for further review.
- **🌐 Interactive Interface:** Use Streamlit to interact with the screening pipeline through a browser.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| DSPy | Structured language-model programming and pipeline orchestration |
| Google Gemini API | AI-powered candidate analysis and job matching |
| Streamlit | Interactive web interface |
| pypdf | Extract text from PDF resumes |
| python-dotenv | Load environment variables securely |
| JSON | Store and export structured evaluation reports |

## 🏗️ Project Structure

```text
RBT23CB019/
├── main.py
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── .env                 # Local configuration; do not commit
```

### File Descriptions

- `main.py` — Defines the DSPy signatures, screening pipeline, and command-line execution flow.
- `app.py` — Provides the Streamlit interface for resume upload, job-description input, and evaluation results.
- `requirements.txt` — Lists the Python dependencies.
- `.env.example` — Provides a template for the required API configuration.
- `.gitignore` — Excludes secrets, virtual environments, and generated files from version control.

## ⚙️ Prerequisites

Before running SmartHireAI, ensure you have:

- Python 3.10 or later, compatible with the installed dependencies.
- pip, the Python package installer.
- A Google Gemini API key.
- An internet connection to access the configured language model.
- A text-based PDF resume for testing.

## 🚀 Installation and Setup

### 1. Clone the Repository

Clone the repository containing the project, then navigate to its directory.

```bash
git clone <your-repository-url>
cd RBT23CB019
```

Replace `<your-repository-url>` with your repository URL. If you have already cloned the repository, navigate directly to the project directory.

### 2. Create a Virtual Environment

**Windows — PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux or macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If you do not yet have a `requirements.txt` file, create one containing:

```text
dspy
python-dotenv
pypdf
streamlit
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project root.

Add the following configuration:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your actual API key.

**Security:** Never commit `.env` or publish your API key. Keep `.env.example` limited to placeholder values.

### 5. Launch the Streamlit Application

Run:

```bash
python -m streamlit run app.py
```

Open the local address displayed in your terminal. By default, Streamlit uses:

```text
http://localhost:8501
```

## 🖥️ How to Use

1. Launch the Streamlit application.
2. Upload a candidate's resume in PDF format.
3. Paste the target job description into the text area.
4. Click **Analyze Resume**.
5. Review the extracted skills, experience summary, and suitable roles.
6. Examine the job-match score and matching skills.
7. Review missing or unverified skills and the match explanation.
8. Review the suggested interview questions.
9. Download the evaluation report as a JSON file.

## 🔄 How the Pipeline Works

SmartHireAI uses a structured, multi-stage DSPy pipeline.

### Stage 1: Candidate Analysis

The `CandidateAnalysis` signature processes the resume and produces:

- Technical skills.
- Experience summary.
- Potentially suitable job roles.
- Supporting resume evidence.

### Stage 2: Job Matching

The `JobMatching` signature receives the resume, job description, and extracted candidate skills. It produces:

- Matching skills.
- Missing or unverified skills.
- An estimated suitability score.
- An explanation of the match.
- Suggested interview questions.

### Stage 3: Report Generation

The `ResumeScreeningPipeline` combines the outputs into a structured report containing candidate analysis, job-matching results, and an evaluation notice.

The Streamlit interface displays the report and provides an option to download it in JSON format.

## 📊 Example Output Structure

The generated report follows a structure similar to this:

```json
{
  "candidate_analysis": {
    "skills": [
      "Python",
      "SQL",
      "Machine Learning"
    ],
    "experience_summary": "Example summary based on resume evidence.",
    "suitable_roles": [
      "Python Developer",
      "Machine Learning Intern"
    ],
    "evidence": [
      "Example evidence extracted from the resume."
    ]
  },
  "job_match": {
    "matching_skills": [
      "Python",
      "SQL"
    ],
    "missing_or_unverified_skills": [
      "Docker"
    ],
    "suitability_score": 75,
    "explanation": "Example explanation of alignment with the job requirements.",
    "interview_questions": [
      "Explain how you have used Python in a project.",
      "How would you use SQL to retrieve data from multiple tables?"
    ]
  },
  "evaluation_notice": "Preliminary AI-generated assessment. Verify findings before making hiring decisions."
}
```

*The values above are illustrative examples, not results from an actual candidate evaluation.*

## 🔐 Privacy and Security

- Store API keys in environment variables rather than source code.
- Exclude `.env`, `.venv/`, Python cache files, and generated reports from Git.
- Obtain appropriate permission before processing candidate resumes.
- Avoid uploading confidential or personally identifiable information to external AI services without appropriate authorization.
- Apply appropriate access controls when deploying the application.

## ⚠️ Limitations

- Resume analysis depends on the quality and readability of the extracted PDF text.
- Scanned PDFs may require OCR, which is not currently implemented.
- AI-generated skills and explanations may be incomplete or inaccurate.
- The suitability score is an estimate and is not a scientifically validated measure of candidate performance.
- API availability, rate limits, and model responses may affect execution.
- The application does not independently verify candidates' qualifications or employment history.

## 🔮 Future Enhancements

Potential improvements include:

- Support for DOCX resumes.
- OCR for scanned resumes.
- Batch processing of multiple resumes.
- Comparison and ranking of candidates against the same job description.
- Persistent storage of evaluation history.
- Improved evaluation metrics and validation.
- More detailed audit trails and evidence-based explanations.
- Authentication and access control for deployed instances.

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome. When contributing:

1. Create a feature branch.
2. Make and test your changes.
3. Keep credentials and confidential candidate information out of commits.
4. Submit a pull request describing your changes.

## ⚖️ Responsible Use

SmartHireAI is intended to support preliminary resume review, not to replace human judgment.

AI-generated results can contain errors and may reflect bias in the model or source data. Review the supporting evidence, apply consistent job-related criteria, and ensure that hiring decisions remain under appropriate human oversight.

**Do not use the generated score as the sole basis for rejecting or selecting a candidate.**

## 📄 License

No license has been specified yet. Add a `LICENSE` file before distributing the project under an open-source license.

---

**Built with Python, DSPy, Gemini, and Streamlit.** 🚀
