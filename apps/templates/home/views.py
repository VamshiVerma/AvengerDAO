import requests # Get the HTML
import random # To select random user agents
import json # Save extracted data from the JSON
import pandas as pd
from time import sleep # Delay between requests
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (X11; Linux i686; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/83.0.4254.27",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/83.0.4254.27",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/83.0.4254.27"
]
def pick_random_user_agent():

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Mozilla/5.0 (X11; Linux i686; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/83.0.4254.27",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/83.0.4254.27",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/83.0.4254.27"
    ]

    header = {"user-agent": random.choice(user_agents)}

    return header
def get_bscscan():
    header = pick_random_user_agent()

    while True:
        response = requests.get(
            "https://bscscan.com/contractsVerified?ps=100",
            headers=header,
            timeout=20
        )

        if response.status_code == 200:
            break
        else:
            header = pick_random_user_agent()

    return response.content
def parse_body(body):
    parsed_body = pd.read_html(body)[0]

    results_array = []
    for i, row in parsed_body.iterrows():
        contract = {
            "position": i,
            "name": row["Contract Name"],
           # "compiler": row["Compiler"],
            #"compiler_version": row["Version"],
            #"license": row["License"],
            #"balance": row["Balance"],
            #"transactions": row["Txns"],
            "address": row["Address"],
            #"contract_url": "https://bscscan.com/address/" + row["Address"],
            #"token_url": "https://bscscan.com/token/" + row["Address"] + "#balances",
            #"holders_url": "https://bscscan.com/token/tokenholderchart/"
            #+ row["Address"]
            #+ "?range=500",
        }

        results_array.append(contract)

    return results_array
x=parse_body(get_bscscan())
type(x)
lst = ['position', 'name']
# Calling DataFrame constructor on list 
dfItem = pd.DataFrame.from_records(x)

l=dfItem['address']
l=l[:10]


import requests
import json
url = "https://www.pipsr.cloud/api/v1/address-security?address=0x9bd547446ea13c0c13df2c1885e1f5b019a77441"

payload = "{\"address\":\"0x9bd547446ea13c0c13df2c1885e1f5b019a77441\"}"
headers = {'Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)
k=response.text
j=json.loads(k)#k=pd.json_normalize(response)

df = pd.json_normalize(j['data'],errors='ignore')
df= df[['trust_level','trust_score']]

for i in l.values:
  print(i)
  url = "https://www.pipsr.cloud/api/v1/address-security?address="+i

  payload = "{\"address\":\""+i+"\"}"
  headers = {'Content-Type': 'application/json'}
  response = requests.request("POST", url, headers=headers, data=payload)
  k=response.text
  j=json.loads(k)#k=pd.json_normalize(response)

  p = pd.json_normalize(j['data'],errors='ignore')
  p= p[['trust_level','trust_score']]
  p['address']=i
  df= df.append(p);
  df= df.append(df.take([1]));

  print(p['address'],p['trust_score'])

from django.shortcuts import render

df=df.drop_duplicates()
df = df.iloc[1:]
df.reset_index(drop=True, inplace=True)
pd.concat([l, df],axis=1)
json_records = df.reset_index().to_json()
data = []
data = json.loads(json_records)
context = {'d': data}
render( 'transactions.html', context)