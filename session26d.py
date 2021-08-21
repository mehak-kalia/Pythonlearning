import requests
import json
import matplotlib.pyplot as plt
response = requests.get("https://api.covid19india.org/data.json")
#print(response.text)

# loads takes json and gives back python dictionary
covid_cases = json.loads(response.text)
covid_cases_statewise = covid_cases['statewise']
print(covid_cases_statewise)

for case in covid_cases_statewise:
   plt.bar(case['state'], case['confirmed'])

plt.show()