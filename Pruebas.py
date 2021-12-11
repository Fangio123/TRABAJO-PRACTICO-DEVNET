import json
import requests
requests.packages.urllib3.disable_warnings()
import urllib.parse
from prettytable import PrettyTable

###1.Obteniendo el id de la organizacioes ### 

print ("1.Obteniendo los id de las Organizaiones ")

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

###2.Buesco un  id de organizacion y obtengo sus Redes ###



IdOrg = response_json[3]["id"]

###print (IdOrg)

main_api="https://api.meraki.com/api/v1/organizations/"
headers={"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}


print ("2.Obteniendo las redes de la organizacion id" ,IdOrg)
api_url2=main_api+(IdOrg)+'/networks'

###VERIFICO LA URL
###print(f"URL:{api_url2}")



resp2 = requests.get(api_url2,headers=headers,verify=False)
print("Request status:",resp2.status_code)

response_json2 = resp2.json()

### Expreso la respuesta al requests en una tabla 

tableRedes = PrettyTable(["id","Redes"])
for redes in response_json2:
    
    tableRedes.add_row([redes["id"],redes["name"]])

print(tableRedes)






###3.Obtengo el id de la red y consulto sus  dispositivos .


IdNet = response_json2[0]["id"]
print ("3.Obteniendo los dispositivos de la Red  id",IdNet)
main_api2="https://api.meraki.com/api/v1/networks/"

###Armado de la URL###
api_url3=main_api2+(IdNet)+'/devices'


resp3 = requests.get(api_url3,headers=headers,verify=False)
print("Request status:",resp3.status_code)
response_json3 = resp3.json()
###print(json.dumps(response_json3, indent=4))

### Armo la tabla para los dispositivos de la Red###

tableDisp = PrettyTable(["Direccion","Nroserie"])
for Dispositivos in response_json3:
    
    tableDisp.add_row([Dispositivos["address"],Dispositivos["serial"]])

print(tableDisp)

###4.Obtener datos de la Red con el Network id

IdNet = response_json2[0]["id"]

print ("4.Obteniendo los datos  de la Red  id",IdNet)

main_api2="https://api.meraki.com/api/v1/networks/"

api_url4=main_api2+(IdNet)

resp4 = requests.get(api_url4,headers=headers,verify=False)
print("Request status:",resp4.status_code)
response_json4 = resp4.json()
Redes1=response_json4["name"]
Redes2=response_json4["timeZone"]

### Armo la tabla para datos de Red 

tableDatosRed = PrettyTable(["Nombre","Zona Horaria"])
   
tableDatosRed.add_row([Redes1,Redes2])

print(tableDatosRed)

### Obtener informacion de un dispositivo de una red con el nro de serie 


IdSerie = response_json3[0]["serial"]
###print (IdSerie)

print ("Obtengo informacion de un dispositivo con el nro de serie",IdSerie)

api_url5=main_api2+(IdNet)+'/devices/'+(IdSerie)


resp5 = requests.get(api_url5,headers=headers,verify=False)
print("Request status:",resp4.status_code)
response_json5 = resp5.json()
###print(json.dumps(response_json5, indent=4))

### Armo la tabla para datos del dispositivo segun nro de serie  

tableNetSerie = PrettyTable(["Direccion","modelo"])
Serie1=response_json5["address"]
Serie2=response_json5["model"] 

    
tableNetSerie.add_row([Serie1,Serie2])

print(tableNetSerie)






print ("Obtengo los SSID para la la Red Id" ,IdNet  )
###6. Obtengo informacion del SSID para el network ID 
api_url6=main_api2+(IdNet)+'/wireless/ssids'
###print (api_url6)

resp6 = requests.get(api_url6,headers=headers,verify=False)
###print("Request status:",resp6.status_code)

response_json6 = resp6.json()
Ssid=response_json6
###print(json.dumps(Ssid, indent=4))

tableWlan = PrettyTable(["Nombre","Seleccion de banda ", "visible"])
for Wlan in Ssid:    
    tableWlan.add_row([Wlan["name"],Wlan["bandSelection"],Wlan["visible"]])

print(tableWlan)






























