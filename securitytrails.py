import requests
import json
import sys

domain = sys.argv[1]

url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"

querystring = {"children_only":"false","include_inactive":"false"}

headers = {
    "Accept": "application/json",
    "APIKEY": ""
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

with open('securitytrails.txt', 'w') as f:
    for subdomain in data['subdomains']:
        f.write(subdomain+"."+domain)
        f.write('\n')