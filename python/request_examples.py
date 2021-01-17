import requests

r = requests.get("https://raw.githubusercontent.com/brettjouwstra/NERC-CIP-2-JSON/master/All_Standards.json")

# Count Number of Entries for CIP-002-5.1

count = 0

for item in r.json():
    if item['Standard'] == "CIP-002-5.1":
        count += 1
print(count)

# Output: 7


# Get a List of Standard Names - Showing only the Unique Entries

standard_name = []
for item in r.json():
    for k,v in item.items():
        if k == 'Standard' and v not in standard_name:
            standard_name.append(v)

# Output: ['CIP-002-5.1', 'CIP-003-8', 'CIP-004-6', 'CIP-005-6', 'CIP-006-6', 'CIP-007-6', 'CIP-008-5', 'CIP-009-6', 'CIP-010-3', 'CIP-011-2', 'CIP-013-1']
