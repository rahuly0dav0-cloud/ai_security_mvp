# sentiment_sandbox/train_and_demo.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
import joblib

# tiny synthetic dataset (quick demo)
X = [
    "i love this product",
    "this is terrible",
    "happy with the service",
    "hate it",
    "not good",
    "excellent work",
    "could be better",
    "very satisfied",
    "worst experience ever",
    "absolutely fantastic"
]
y = [1,0,1,0,0,1,0,1,0,1]

pipe = make_pipeline(TfidfVectorizer(), SVC(probability=True))
pipe.fit(X, y)
joblib.dump(pipe, "sentiment_model.joblib")
print("Model trained and saved to sentiment_model.joblib")

# quick demo predictions
tests = [
    "I absolutely love this!",
    "This is awful and bad",
    "Not bad, could be better"
]
for t in tests:
    pred = pipe.predict([t])[0]
    prob = pipe.predict_proba([t])[0].max()
    label = "positive" if pred == 1 else "negative"
    print(f"'{t}' -> {label} (prob={prob:.2f})")