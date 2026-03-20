# Phish Detect AI 🔒

Simple ML project to detect phishing URLs/emails using Python & scikit-learn.  
Focus: clean code, feature engineering, CLI inference.

## Features
- Custom features (lexical + content) in `src/phishdetect/features.py`
- RandomForest model (train: `src/phishdetect/train.py`)
- CLI inference (run: `src/phishdetect/infer.py`)
- Reproducible environment with `requirements.txt`

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
