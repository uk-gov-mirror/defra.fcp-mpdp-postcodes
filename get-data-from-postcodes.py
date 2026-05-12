import sys

import pandas as pd
import requests
import urllib

if len(sys.argv) < 2:
    print("Usage: python3 Script.py <input_csv_file>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]

data = pd.read_csv(input_file, encoding="latin-1", low_memory=False)
data["part_postcode"] = data["part_postcode"].fillna("")

has_full_postcode = "full_postcode" in data.columns
if has_full_postcode:
    data["full_postcode"] = data["full_postcode"].fillna("")

baseUrl = "http://localhost:8000"

for index, row in data.iterrows():
    full = row["full_postcode"].strip() if has_full_postcode else ""
    part = row["part_postcode"].strip()

    if full:
        request_url = baseUrl + "/postcodes/" + urllib.parse.quote(full)
        query = requests.get(request_url)

        if query.json()['status'] != 200:
            print(",")
            continue

        result = query.json()['result']
        parliamentary_constituency = result['parliamentary_constituency'] or ""
        admin_county = result['admin_county'] or ""

        print(f"{parliamentary_constituency},{admin_county}")
    elif part:
        request_url = baseUrl + "/outcodes/" + urllib.parse.quote(part)
        query = requests.get(request_url)

        if query.json()['status'] != 200:
            print(",")
            continue

        result = query.json()['result']
        parliamentary_constituency = result['parliamentary_constituency'][0] if len(result['parliamentary_constituency']) == 1 else ""
        admin_county = result['admin_county'][0] if len(result['admin_county']) == 1 else ""

        print(f"{parliamentary_constituency},{admin_county}")
    else:
        print(",")
