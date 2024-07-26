import requests
import json
import sys

args = sys.argv

id = args[1]

url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={id}"

response = requests.get(url)

cvssv3 = None
data = json.loads(response.text)
for cve in data["vulnerabilities"]:
    cveid = cve['cve']['id']
    try:
        cvssv3 = cve['cve']['metrics']['cvssMetricV31'][0]['cvssData']['baseScore']
    except KeyError:
        pass
    cvssv3 = cvssv3 or 0.0
    print(f"{cveid},{cvssv3}")
