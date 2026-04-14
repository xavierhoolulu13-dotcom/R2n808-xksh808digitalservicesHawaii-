def explain(code):
    return {"explanation": f"This code does: {code[:60]}..."}

def stub(name):
    return f"def {name}():\n    pass"
