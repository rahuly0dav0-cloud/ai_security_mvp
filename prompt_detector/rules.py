# rules.py
KEYWORDS = [
    "ignore previous",
    "disregard previous instructions",
    "follow these instructions",
    "jailbreak",
    "bypass",
    "ignore safety",
    "system prompt",
    "do anything"
]

REGEX_PATTERNS = [
    r"ignore (?:my )?previous instructions",
    r"follow these instructions exactly",
    r"translate this prompt and execute",
    r"if you are an assistant, (?:then )?respond with"
]