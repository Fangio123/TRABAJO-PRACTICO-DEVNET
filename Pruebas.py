import json
import requests
requests.packages.urllib3.disable_warnings()
import urllib.parse
from prettytable import PrettyTable

###para obtener las organizaciones ME RESULTA SIN PROBLEMAS### 

api_url="http://api.meraki.com/api/v1/organizations"
headers={"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

resp = requests.get(api_url,headers=headers,verify=False)
print("Request status:",resp.status_code)

response_json = resp.json()
###imprimo el Json como  tabla


table = PrettyTable(["Id","Organizaciones"])
for Organiz in response_json:
    table.add_row([Organiz["id"],Organiz["name"]])

print(table)

###buesco el id de organizacion  ###

IdOrg = response_json[3]["id"]

print (IdOrg)



main_api="https://api.meraki.com/api/v1/organizations/"
headers={"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}


print ("Obteniendo las redes de la organizacion id" ,IdOrg)
api_url2=main_api+(IdOrg)+'/networks'

###VERIFICO LA URL
###print(f"URL:{api_url2}")



resp2 = requests.get(api_url2,headers=headers,verify=False)
print("Request status:",resp2.status_code)

response_json2 = resp2.json()

tableRedes = PrettyTable(["id","Redes"])
for redes in response_json2:
    
    tableRedes.add_row([redes["id"],redes["name"]])

print(tableRedes)






###Obtengo el id de la red y consulto sus  dispositivos .
IdNet = response_json2[0]["id"]
print (IdNet)
main_api2="https://api.meraki.com/api/v1/networks/"

###Armado de la URL###
api_url3=main_api2+(IdNet)+'/devices'


resp3 = requests.get(api_url3,headers=headers,verify=False)
print("Request status:",resp3.status_code)
response_json3 = resp3.json()
###print(json.dumps(response_json3, indent=4))

### armo la tabla ###

tableDisp = PrettyTable(["Direccion","Nroserie"])
for Dispositivos in response_json3:
    
    tableDisp.add_row([Dispositivos["address"],Dispositivos["serial"]])

print(tableDisp)



















