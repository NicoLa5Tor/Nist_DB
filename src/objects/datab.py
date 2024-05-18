import requests
import os,json
class Database:
    def __init__(self) :
        self.uril = self.url()
    def url(self):
        with open('config.json','r') as conf:
            data = json.load(conf)
            return data['urlDb']
        
    def add_per_Month(self,obj):
        data = {
                "name_db" : "NicolasJuan",
                "_id" : "Vulns_Per_Month",
                "name_collection" : "Content",
                "item" : obj 
                }
        status = self.add_db(dt=data)
        if status == 201:
            print("Datos ingresados")
        elif status == 409:
            self.update_db(dt=data)
    def update_db(self,dt):
        uril = self.uril + "/update_item"
        try:
            response = requests.put(url=uril,json=dt)
            if response.status_code == 200:
                print(response.json())
            print(response)
        except Exception as e:
            print(e)
    def add_db(self,dt):
        uril = self.uril + "/add_item" 
        try:
            response = requests.post(url=uril,json=dt)
            return response.status_code
        except Exception as e:
            print(f"Acurrio un error {str(e)}")
            return 0
    

    def concat_new_vulns(self,none, low, medium, high, critical, awaitAnalisis,total):
        
        item_json_get = self.seach_db()
        if item_json_get is None:
            print("El dato devuelto es nulo")
        newnone = none+item_json_get['None']
        newlow = low+item_json_get['Low']
        newmedium = medium+item_json_get['Medium']
        newhigh = high+item_json_get['High']
        newcritical = critical+item_json_get['Critical']
        newawaitAnalisis = awaitAnalisis+item_json_get['AwaitAnalisis']
        newTotal = total+item_json_get['Total']
        
        try:
            data = {
                "name_db" : "NicolasJuan",
                "_id" : "Count_Vulns",
                "name_collection" : "Content",
                "item" : {
                    "None" : newnone,
                    "Low" : newlow,
                    "Medium" : newmedium,
                    "High" : newhigh,
                    "Critical" : newcritical,
                    "AwaitAnalisis" : newawaitAnalisis,
                    "Total" : newTotal
                }
            }
            self.add_db(dt=data)

        except Exception as e:
            print(f"Error al guardar los nuvos datos {str(e)}")




    def seach_db(self):
        data = {
            "name_db" : "NicolasJuan",
            "_id" : "Count_Oldvulns",
            "name_collection" : "Content"
        }
        try:
            url = self.uril + "/get_item"
            print(f"la url es {url}")
            response = requests.get(url=url,json=data)
            if response.status_code == 200:
                dat = response.json()
                print(dat)
                print("retorna el get item")
                return dat['response']['item']
            else:
                print("algun error de acceso al consulatar")
                return None

        except Exception as e:
            print(f"Error al cunsultar la base para en busca del item {str(e)}")
            return None