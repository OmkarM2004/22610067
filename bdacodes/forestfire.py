# forestfire_mapreduce.py
# Simulated MapReduce in Python (no Hadoop needed)

import csv
from collections import defaultdict

# ---------- MAPPER FUNCTION ----------
def mapper(row):
    """Reads one record and emits a key-value pair."""
    month = row['month']
    temp = float(row['temp'])
    return month, temp


# ---------- REDUCER FUNCTION ----------
def reducer(mapped_data):
    """Groups by key and calculates average temperature."""
    grouped = defaultdict(list)
    for key, value in mapped_data:
        grouped[key].append(value)

    # Calculate average per key
    reduced = {key: sum(values) / len(values) for key, values in grouped.items()}
    return reduced


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    # Load dataset (make sure path is correct)
    with open(r"C:\Users\omman\Desktop\my_genai_code\forestfires.csv") as f:
        reader = csv.DictReader(f)
        mapped = [mapper(row) for row in reader]

    # Reduce phase
    results = reducer(mapped)

    print("🔥 Average Temperature per Month (MapReduce Simulation):")
    for month, avg_temp in results.items():
        print(f"{month}: {avg_temp:.2f}")
