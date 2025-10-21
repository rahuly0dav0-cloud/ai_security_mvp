from fastapi import FastAPI
from pydantic import BaseModel
import re
from rules import KEYWORDS, REGEX_PATTERNS

app = FastAPI()

class PromptIn(BaseModel):
    text: str

def score_and_flags(text: str):
    lowered = text.lower()
    flags = []
    score = 0.0
    for k in KEYWORDS:
        if k in lowered:
            flags.append({"type": "keyword", "value": k})
            score += 0.2
    for p in REGEX_PATTERNS:
        if re.search(p, lowered):
            flags.append({"type": "pattern", "value": p})
            score += 0.3
    return min(1.0, score), flags

@app.post("/detect")
def detect(inp: PromptIn):
    s, flags = score_and_flags(inp.text)
    return {"score": s, "flags": flags}