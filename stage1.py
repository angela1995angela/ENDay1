import requests
import json

merakikey = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
base_url = 'https://api.meraki.com/api/v0'
endpoint = '/organizations'

headers = {
    'X-Cisco-meraki-API-Key': merakikey
}


try:
    response = requests.get(url=f"{base_url}{endpoint}", headers=headers)
    if response.status_code == 200:
        orgs = response.json()
        for org in  orgs:
            if org['name']== 'DevNet Sandbox':
                orgID = org['id']
except Exception as ex:
    print(ex)


endpoint2 = f"/organizations/{orgID}/networks"

try:
    response = requests.get(url=f"{base_url}{endpoint2}", headers=headers)
    if response.status_code == 200:
        nets = response.json()
        for net in nets:
            if net['name'] == 'DevNet Sandbox ALWAYS ON':
                netID = net['id']
except Exception as ex2:
    print(ex2)


endpoint3 = f"/networks/{netID}/devices"

try:
    response = requests.get(url=f"{base_url}{endpoint3}", headers=headers)
    if response.status_code == 200:
        devices = response.json()
except Exception as ex3:
    print(ex3)

print(json.dumps(response, indent=2))
file1= open('stage1.txt','w')


for dev in devices:
    file1.write(f"Type {dev['model']}\nMACaddress {dev['mac']}\nSerialNumber {dev['serial']}\n")
    
file1.close()
