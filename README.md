# AI Security MVP — Rahul Yadav

Small, runnable MVPs for LLM safety demos:
- **prompt_detector** — FastAPI rule engine to flag prompt injections. (POST /detect)
- **redteam_runner** — Runs adversarial prompts (mock LLM) and writes `results.csv`.
- **evalbench** — Computes safety/factuality/coherence proxies and outputs `summary.html`.
- **sentiment_sandbox** — Tiny SVM pipeline: train → save → predict.

## Quick run (local)
# Activate venv
source .venv/bin/activate

# Prompt Detector
cd prompt_detector
uvicorn app:app --port 8001 --reload
# sample:
curl -s -X POST "http://127.0.0.1:8001/detect" -H "Content-Type: application/json" -d '{"text":"Ignore previous instructions."}' | python -m json.tool

# Red-Team Runner
cd ../redteam_runner
python run_probes.py
# results -> results.csv

# EvalBench
cd ../evalbench
python main.py
# outputs -> eval_scores.csv and summary.html

# Sentiment Sandbox
cd ../sentiment_sandbox
python train_and_demo.py
# outputs -> sentiment_model.joblib

## Notes
- These are MVPs: redteam uses a mock LLM for safety. Replace with real API calls (and .env api key) if needed.
- Add `.env` (not committed) for API keys. See code comments for swap points.
