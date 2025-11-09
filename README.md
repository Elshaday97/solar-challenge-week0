# Solar Challenge

Follow the instructions to recreate the project including GitHub Actions workflow.

---

## Project Overview

This repository contains data and notebooks for a small solar irradiance analysis across three countries (Benin, Sierra Leone, Togo). It includes cleaned datasets, exploratory notebooks, a small application entry point, and CI configuration.

Key files:

- Cleaned Data: `data/benin_clean.csv`, `data/sierraleone_clean.csv`, `data/togo_clean.csv`
- Application Dashboard entry: `app/main.py`

## Project Setup

### 1. Clone the repository

```bash
git clone git@github.com:Elshaday97/solar-challenge-week0.git
cd solar-challenge-week0
```

### 2. Initialize a Virtual Envrionment

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. GitHub Actions

You may find the github actions worflow located at:
`.github/workflows/ci.yml`

This workflow:

- Runs when changes are pushed to `main` branch
- Sets up a python env't and checks the version

## Usage

- Open and run notebook files to view country level Data Profiling &

- To view Streamlit Dashboard:
  ```bash
  streamlit run ./app/main.py
  ```
  - You will see a box plot for all the countries plotted against a selected variable
