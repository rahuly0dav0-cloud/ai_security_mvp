# run_probe.py - simple red-team runner (mock LLM)
import csv, json, time, os

PROBES = json.load(open("probes.json", "r", encoding="utf-8"))

def query_mock(prompt):
    # Simple mock: mark unsafe if trigger words appear
    lowered = prompt.lower()
    unsafe_triggers = ["ignore previous", "reveal", "admin", "credentials", "exfiltrate", "secret", "api key", "bypass", "cat /etc/passwd"]
    is_unsafe = any(t in lowered for t in unsafe_triggers)
    if is_unsafe:
        response = "[UNSAFE] Request denied or redacted."
    else:
        response = "[SAFE] Generic informational response."
    return {"text": response, "unsafe": is_unsafe}

def run():
    out_path = "results.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["prompt","response","unsafe","timestamp"])
        writer.writeheader()
        for p in PROBES:
            ts = time.time()
            r = query_mock(p)
            writer.writerow({
                "prompt": p,
                "response": r["text"],
                "unsafe": int(r["unsafe"]),
                "timestamp": ts
            })
    print(f"Done. Wrote {out_path}")

if __name__ == "__main__":
    run()