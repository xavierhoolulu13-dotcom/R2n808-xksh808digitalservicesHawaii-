def to_table(text):
    return [row.split(",") for row in text.split("\n")]

def stats(nums):
    return {
        "count": len(nums),
        "min": min(nums),
        "max": max(nums),
        "avg": sum(nums) / len(nums)
    }
