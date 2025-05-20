# AI Career Recommender System

An AI-powered career recommender that analyzes user text or resume content to suggest the best-fitting career paths.

## Features
- Upload your resume in PDF or describe your interests
- Get top 3 career suggestions based on NLP + ML
- Streamlit-based web interface

## Installation
```bash
git clone https://github.com/yourusername/ai-career-recommender.git
cd ai-career-recommender
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

## Sample Output
> **Recommended Careers:**
> - Data Scientist: 92.4%
> - AI/ML Engineer: 89.1%
> - Product Manager: 70.3%

## Folder Structure
```
project/
├── app.py
├── main.py
├── resume_parser.py
├── requirements.txt
├── utils.py
├── sample_resume.pdf
└── README.md
```

## License
MIT
