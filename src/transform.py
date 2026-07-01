import pandas as pd
from extract import extract_data
from extract import fetch_region_names

def transform_data(data):
    region_names = fetch_region_names()
    records = data['data']
    rows = []
    for record in records:
        region = record['key'][0]
        region_name = region_names[region]
        year = int(record['key'][1])    
        population = int(record['values'][0])
        if record['values'][1] == '..':
            growth = None
        else:
            growth = int(record['values'][1])
        rows.append({
            "region": region,
            "region_name": region_name,
            "year": year,
            "population": population,
            "growth": growth

        })
    df = pd.DataFrame(rows)
    return df

if __name__ == "__main__":
    data = extract_data(["00","01", "03"])
    result = transform_data(data)
    print(result)