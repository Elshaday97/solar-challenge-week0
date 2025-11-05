# Solar Challenge

Follow the instructions to recreate the project including GitHub Actions workflow.

---

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
