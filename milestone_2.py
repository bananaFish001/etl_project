import json

with open("case.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

parsed_records = []

for record in raw_data:
    payload_str = record['Payload']
    payload_dict = json.loads(payload_str)
    parsed_records.append(payload_dict)

# Sanity check: look at the first unpacked payload
print(type(parsed_records[0]))
print(json.dumps(parsed_records[0], indent=2)[:1000])

# Try reaching directly into a nested field now that it's a real dict
print(parsed_records[0]["OfferId"])
print(parsed_records[0]["CuratedOfferOptions"])
