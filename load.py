import json

# Step 1: Load raw JSON
with open("case.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# Step 2: What's the top-level type?
print(type(raw_data))

# Step 3: If it's a list, inspect the first record
if isinstance(raw_data, list):
    first_record = raw_data[0]
    print(json.dumps(first_record, indent=2)[:1000])  # pretty-print, capped length
elif isinstance(raw_data, dict):
    print(list(raw_data.keys()))
