import requests
import pandas as pd
import time
from pathlib import Path
from tqdm import tqdm
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("Missing GROQ_API_KEY. Please add it in your .env file")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-70b-8192"
FUNCTION_FOLDER = "gretel_and_dirty_functions"
TESTCASE_FILE = Path(__file__).parent / "rq4_testcases.csv"
CWE_FILE = Path(__file__).parent / "CWE_LIST.csv"
OUTPUT_CSV = Path(__file__).parent / "rq4_results.csv"

def build_rq4_prompt(code: str) -> str:
    return f"""You are a cybersecurity expert.
Analyze the following Python function for security vulnerabilities. 
- Identify clearly the SINGLE MOST RELEVANT CWE from the official CWE list.
- Describe the vulnerability explicitly using the CWE's official name.
Answer strictly in this format:

CWE-ID: CWE-XXX
Description: [Official CWE Name + short explanation]

Function:
{code}
Answer:
"""

def ask_llama3(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0, 
        "max_tokens": 128
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

def run_rq4():
    df = pd.read_csv(TESTCASE_FILE, encoding="utf-8")
    print(" Colonne rilevate nel CSV:", df.columns.tolist())

    results = []

    for _, row in tqdm(df.iterrows(), total=len(df), desc="RQ4 Evaluation"):
        filename = row["filename"]
        cwe_target = row.get("CWE_TARGET", "")

        path = Path(FUNCTION_FOLDER) / filename
        if not path.exists():
            print(f" File non trovato: {filename}")
            continue

        code = path.read_text()
        prompt = build_rq4_prompt(code)

        try:
            response = ask_llama3(prompt)
        except Exception as e:
            response = f"Errore: {e}"

        results.append({
            "filename": filename,
            "CWE_Target": cwe_target,
            "RQ4_Description": response
        })

        time.sleep(4) 

    pd.DataFrame(results).to_csv(OUTPUT_CSV, index=False)
    print(f"\n RQ4 completata. Risultati salvati in {OUTPUT_CSV}")

if __name__ == "__main__":
    run_rq4()
