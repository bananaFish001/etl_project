import json

# 1: Load raw json
with open("case.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# 2. Datatype of the data
print(type(raw_data))
# print(json.dumps(raw_data[0], indent=2)[:1000])

if isinstance(raw_data, list):
    first_record = raw_data[0]
    print(json.dumps(first_record, indent=2)[:1000])
if isinstance(raw_data, dict):
    print(list(raw_data.keys()))
