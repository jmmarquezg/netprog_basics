import requests
import json
from pprint import pprint


url = "https://dashboard.meraki.com/api/v0/organizations"
headers = {'X-Cisco-Meraki-API-key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'}

#Requests para obtener las organizaciones
organizations = requests.get(url, headers=headers)

for organization in organizations.json():
    if organization["id"] == "549236":
        network_name = organization["name"]

#Creando url para mandar un request a la red que obtubimos en el request anterior
url2 = "https://dashboard.meraki.com/api/v0/organizations/{}/networks".format(organization["id"])

networks = requests.get(url2, headers=headers)
for network in networks.json():
    if network["name"] == "San Jose Lab":
        network_id = network["id"]
pprint(network_id)

#Creando la url para obtener el inventario de una organizacion
url3 = "https://dashboard.meraki.com/api/v0/organizations/{}/inventory".format(organization["id"])
inventory = requests.get(url3, headers=headers)

pprint(inventory.json())
for device in inventory.json():
    device_name = device["name"]
    device_model = device["model"]
    output = "Device Name: " + device_name + "\tDevice Model: " + device_model
    print(output.expandtabs(30))