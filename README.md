````markdown
# Automated Code Review with LLaMA 3 via Groq

Bachelor’s thesis (UNISA). I use **LLaMA 3 (70B)** via **Groq API** to automate code review in fintech: detect vulnerabilities, verify functional correctness, decide **Approve/Reject** with Chain-of-Thought, and classify weaknesses by **CWE**. Tech used: **Python 3.9+**, Groq OpenAI-compatible endpoint, embeddings (**all-MiniLM-L12-v2**, **all-mpnet-base-v2**, **BAAI/bge-base-en-v1.5**). Results are saved as CSV.

**Download / Run**
1. Download ZIP from GitHub (**Code → Download ZIP**) **or** clone:
   ```bash
   git clone https://github.com/NicolaAnnu/LLMTHESISGROQthesis.git
   cd LLMTHESISGROQthesis
````

2. Install deps:

   ```bash
   pip install -r requirements.txt
   ```
3. Create `.env` (not tracked by git):

   ```
   GROQ_API_KEY=your_api_key_here
   ```
4. Run a module (examples):

   ```bash
   python RQ1/rq1_runner
   python RQ2/rq2_RunnerFewShot
   python RQ3/rq3_RunnerChainOfThought
   python RQ4/rq4_Runner.py
   ```

**Author:** Nicola Annunziata — University of Salerno (A.Y. 2024/2025)

```
```
