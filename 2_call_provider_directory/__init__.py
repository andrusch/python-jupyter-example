import requests

url = "https://production.api.centene.com/fhir/providerdirectory/Practitioner?family=andrus"

payload={}
headers = {
  'Content-Type': 'application/json'
}
print("Start Data Retrieval")
response = requests.request("GET", url, headers=headers, data=payload)
print("Data Retrieved")
data = response.json()
print("Data Parsed")
for i in range(len(data["entry"])):
  print(data["entry"][i]["resource"]["name"][0]["text"])
