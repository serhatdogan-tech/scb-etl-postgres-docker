import requests


def extract_data(region_code):
    query = [{ "code": "Region", "selection": { "filter": "item", "values": region_code }},
        { "code": "Tid", "selection": { "filter": "top", "values": ["60"] } }]
    payload = { "query": query, "response": {"format": "json"} }

    r = requests.post('https://api.scb.se/OV0104/v1/doris/sv/ssd/START/BE/BE0101/BE0101A/BefolkningNy', json=payload)
    return r.json() 
    #return r.text

def fetch_region_names():
    r = requests.get('https://api.scb.se/OV0104/v1/doris/sv/ssd/START/BE/BE0101/BE0101A/BefolkningNy')
    metadata = r.json()
    region_var = metadata['variables'][0]
    return dict(zip(region_var['values'], region_var['valueTexts']))

if __name__ == "__main__":
    region_data = extract_data(["00","01", "03", "04", "05",
                                 "06", "07", "08", "09", "10",
                                 "12", "13", "14", "17", "18",
                                 "19", "20", "21", "22", "23",
                                 "24", "25"])
    print(region_data)
    print(region_data.keys())
    print(fetch_region_names())