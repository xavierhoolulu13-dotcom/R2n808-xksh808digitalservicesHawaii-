def summarize(text):
    lines = text.split("\n")
    return {"summary": [line.strip() for line in lines if line.strip()]}

def clean(text):
    return " ".join(text.split())
