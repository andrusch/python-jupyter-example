import requests

url = "https://production.api.centene.com/fhir/providerdirectory/InsurancePlan?name=az"

payload={}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
