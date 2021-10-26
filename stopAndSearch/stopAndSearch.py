import requests
import json

def getRatio(force):
    date='2020-01'
    parameters = {
    "date": '2020-01',
    "force": force
    }
    response = requests.get("https://data.police.uk/api/stops-force", params=parameters)
    jresponse = response.json()
    count = 0
    blackCount = 0
    if len(jresponse) == 0:
        print("No data for " + force)
        return
    for i in jresponse:
        count += 1
        ethnicity = i['self_defined_ethnicity']
        if ethnicity is None:
            continue
        elif "Black" in str(ethnicity):
            blackCount += 1
    ratio = round(blackCount/count*100,2)
    print("Proportion of stop and search involving black citizens for " + force + ": " + str(ratio) + "%")

forces = []
jforces = requests.get("https://data.police.uk/api/forces")
for i in jforces.json():
    forces.append(i['id'])

for force in forces:
    getRatio(force)