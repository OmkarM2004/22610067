# forestfire.py
# Simulated MapReduce in Python (no Hadoop needed)

import csv
from collections import defaultdict

# ---------- MAPPER FUNCTION ----------
def mapper(row):
    """
    Reads one record and emits a key-value pair.
    Example: key = Month, value = Temperature_Celsius
    """
    month = row['Month']
    temp = float(row['Temperature_Celsius'])
    return month, temp


# ---------- REDUCER FUNCTION ----------
def reducer(mapped_data):
    """
    Groups by key and calculates average temperature.
    """
    grouped = defaultdict(list)
    for key, value in mapped_data:
        grouped[key].append(value)

    # Calculate average per key
    reduced = {key: sum(values)/len(values) for key, values in grouped.items()}
    return reduced


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    # Load dataset (ensure forestfires.csv is in same folder)
    with open(r"C:\Users\omman\Desktop\my_genai_code\forestfires.csv") as f:
        reader = csv.DictReader(f)
        mapped = [mapper(row) for row in reader]

    # Reduce phase
    results = reducer(mapped)

    print("🔥 Average Temperature per Month (MapReduce Simulation):")
    for month, avg_temp in results.items():
        print(f"{month}: {avg_temp:.2f}")
