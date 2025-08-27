# Simple Python Calculator

A beginner-friendly CLI calculator with add, subtract, multiply, and divide.

## Run locally

```bash
python3 app.py
```

## Project structure
```text
python-calculator/
├── app.py              # CLI app
├── calculator.py       # Core functions
├── tests/
│   └── test_calculator.py
├── .github/workflows/python-tests.yml  # Optional CI
└── .gitignore
```

## Tests
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

## Upload to GitHub
1. Create a new repository on GitHub (without adding files).
2. In this folder, run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: simple calculator"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```
