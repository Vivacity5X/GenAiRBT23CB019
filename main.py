import os
import json
from pathlib import Path

import dspy
from dotenv import load_dotenv


# 1. Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "your_actual_api_key_here":
    raise ValueError(
        "Please configure your actual GEMINI_API_KEY in the .env file."
    )


# 2. Configure the language model
lm = dspy.LM(
    "gemini/gemini-3.8-flash",
    api_key=API_KEY
)

dspy.configure(lm=lm)


# 3. Define the candidate analysis task
class CandidateAnalysis(dspy.Signature):
    """Extract candidate skills and identify suitable job roles."""

    resume_text: str = dspy.InputField(
        desc="Full text of the candidate's resume"
    )

    skills: list[str] = dspy.OutputField(
        desc="Technical skills supported by the resume"
    )

    experience_summary: str = dspy.OutputField(
        desc="Summary of the candidate's demonstrated experience"
    )

    suitable_roles: list[str] = dspy.OutputField(
        desc="Potential job roles based on the demonstrated skills"
    )

    evidence: list[str] = dspy.OutputField(
        desc="Evidence taken from the resume"
    )


# 4. Define the job matching task
class JobMatching(dspy.Signature):
    """Evaluate resume alignment with a job description."""

    resume_text: str = dspy.InputField()
    job_description: str = dspy.InputField()
    candidate_skills: list[str] = dspy.InputField()

    matching_skills: list[str] = dspy.OutputField(
        desc="Job requirements supported by resume evidence"
    )

    missing_or_unverified_skills: list[str] = dspy.OutputField(
        desc="Job requirements not demonstrated in the resume"
    )

    suitability_score: int = dspy.OutputField(
        desc="Estimated job requirement match from 0 to 100"
    )

    explanation: str = dspy.OutputField(
        desc="Evidence-based explanation of the match"
    )

    interview_questions: list[str] = dspy.OutputField(
        desc="Questions to verify relevant skills"
    )


# 5. Build the screening pipeline
class ResumeScreeningPipeline(dspy.Module):

    def __init__(self):
        super().__init__()

        self.analyze_candidate = dspy.Predict(
            CandidateAnalysis
        )

        self.match_job = dspy.Predict(
            JobMatching
        )

    def forward(self, resume_text, job_description):

        # Stage A: Extract candidate information
        candidate = self.analyze_candidate(
            resume_text=resume_text
        )

        # Stage B: Match against job requirements
        match = self.match_job(
            resume_text=resume_text,
            job_description=job_description,
            candidate_skills=candidate.skills
        )

        score = max(
            0,
            min(100, int(match.suitability_score))
        )

        # Stage C: Generate structured report
        report = {
            "candidate_analysis": {
                "skills": candidate.skills,
                "experience_summary": candidate.experience_summary,
                "suitable_roles": candidate.suitable_roles,
                "evidence": candidate.evidence
            },
            "job_match": {
                "matching_skills": match.matching_skills,
                "missing_or_unverified_skills":
                    match.missing_or_unverified_skills,
                "suitability_score": score,
                "explanation": match.explanation,
                "interview_questions": match.interview_questions
            },
            "evaluation_notice": (
                "Preliminary AI-generated assessment. "
                "Verify findings before making hiring decisions."
            )
        }

        return report


# 6. Read input files
def read_file(filename):

    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(
            f"Input file not found: {filename}"
        )

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError(f"Input file is empty: {filename}")

    return content


# 7. Execute the application
def main():

    print("=" * 55)
    print("SmartHireAI - DSPy Resume Screening Pipeline")
    print("=" * 55)

    resume_text = read_file("resume.txt")
    job_description = read_file("job_description.txt")

    print("\n[1/3] Analyzing candidate skills...")

    pipeline = ResumeScreeningPipeline()

    print("[2/3] Matching candidate with the job description...")

    report = pipeline(
        resume_text=resume_text,
        job_description=job_description
    )

    print("[3/3] Generating evaluation report...")

    output_path = Path("candidate_evaluation_report.json")

    output_path.write_text(
        json.dumps(report, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )

    print("\n" + "=" * 55)
    print("CANDIDATE EVALUATION REPORT")
    print("=" * 55)

    print(json.dumps(report, indent=4, ensure_ascii=False))

    print("\nReport saved to:", output_path.resolve())


if __name__ == "__main__":
    main()
