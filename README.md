#  Automated Code Review with LLaMA 3 via Groq
##  Project Description

This project constitutes the **Bachelor's Thesis in Computer Science (UNISA)** and proposes an *automated code review* system based on **LLaMA 3 (70B)** executed through **Groq API**.  
The goal is to analyze Python functions in the **fintech** domain to:

- identify security vulnerabilities (RQ1);  
- verify functional correctness of code (RQ2);  
- autonomously decide *Approve / Reject* leveraging Chain-of-Thought reasoning (RQ3);  
- classify weaknesses according to the **CWE** taxonomy (RQ4).
For **RQ4** (CWE Classification), the system uses the **699.csv** file containing all existing CWE (Common Weakness Enumeration) entries. This comprehensive dataset enables the model to classify identified vulnerabilities according to the official CWE taxonomy.

The system combines "clean" data (Gretel) with ad-hoc generated "dirty" functions and saves results in structured CSV files.

---

##  Technologies Used

- **Python 3.9+** – main language  
- **Groq API** – OpenAI-compatible endpoint for high-speed inference  
- **LLaMA 3 (70B)** – Large Language Model used for analysis  
- **Sentence-Transformers** – embedding models `all-MiniLM-L12-v2`, `all-mpnet-base-v2`, `bge-base-en-v1.5`  
- **CSV / dotenv / pandas** – for managing results and environment variables  

---

##  Requirements

Make sure you have installed:

- **Python 3.9 or higher**  
- **pip** for package management  
- A **Groq** account and a valid **API Key**  

---

##  Execution Instructions

1. **Clone the repository**
```bash
   git clone https://github.com/NicolaAnnu/LLMTHESISGROQthesis.git
   cd LLMTHESISGROQthesis
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Create the .env file (not tracked by Git)**
```
   GROQ_API_KEY=your_api_key
```

4. **Run a research module**
```bash
   python RQ1/rq1_runner
   python RQ2/rq2_RunnerFewShot
   python RQ3/rq3_RunnerChainOfThought
   python RQ4/rq4_Runner.py
```

---

## Main Results

| Research | Description | Results |
|----------|--------------|------------|
| **RQ1** | Vulnerability Detection | Accuracy **95.6%** · Recall **100%** |
| **RQ2** | Functional Verification (Few-Shot) | F1 **80.9%** (↑ from 67.2%) |
| **RQ3** | Approve/Reject (CoT) | Accuracy **93.1%** |
| **RQ4** | CWE Classification (MiniLM) | Top-1 **77.5%** · Top-5 **87.5%** |

---

## Project Structure
```
RQ1/ → Vulnerability Detection
RQ2/ → Functional Correctness (One-Shot / Few-Shot)
RQ3/ → Approve-Reject Decision (Chain-of-Thought)
RQ4/ → CWE Classification & CSV Outputs
```