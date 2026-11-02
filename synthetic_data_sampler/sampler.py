"""Schema-driven synthetic record generator with privacy noise."""
import random
from typing import List, Dict, Any

FIRST_NAMES = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones"]

def generate_synthetic_records(count: int = 10, noise_scale: float = 0.1) -> List[Dict[str, Any]]:
    records = []
    for i in range(count):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        # Add slight Laplace-style noise to score
        score = max(0.0, min(100.0, random.gauss(75.0, 10.0) + random.uniform(-noise_scale, noise_scale)))
        records.append({
            "id": i + 1,
            "name": f"{first} {last}",
            "email": f"{first.lower()}.{last.lower()}{random.randint(10, 99)}@example.com",
            "score": round(score, 2)
        })
    return records
