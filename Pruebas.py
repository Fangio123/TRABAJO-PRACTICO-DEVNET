import json
import requests
requests.packages.urllib3.disable_warnings()
import urllib.parse

###para obtener las organizaciones ME RESULTA SIN PROBLEMAS### 

api_url="http://api.meraki.com/api/v1/organizations"
headers={"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

resp = requests.get(api_url,headers=headers,verify=False)
print("Request status:",resp.status_code)

response_json = resp.json()
print(json.dumps(response_json, indent=4))



###en este paso donde surje el error 404 ###

main_api="https://api.meraki.com/api/v1/organizations"
headers={"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

###le asigno a organizacion un numero fijo 463308 *solo para 
###probar  , 
###que en realidad lo obtengo de recorrer el 1er requests 
###json , y se lo asignaria a la variable Organizacion
### mediante la funcion recursiva que vimos en clase .


Organizacion=463308
Redes="/networks"

###Construyo la nueva URL con la organizacion elejida 
###para obteener todas las redes de esa organizacion 

### ES PROBABLE QUE AQUI SE ENCUENTRE EL ERROR 


api_url2=main_api + urllib.parse.urlencode({"/":Organizacion})+Redes

resp2 = requests.get(api_url2,headers=headers,verify=False)
print("Request status:",resp2.status_code)

response_json2 = resp2.json()
print(json.dumps(response_json2, indent=4))




