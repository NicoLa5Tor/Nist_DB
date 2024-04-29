import os,json,datetime
from ..nist_api.api import NistApi


class OperationOs:
    #la clase pide como unico dato opt con el fin de realizar un objeto exclusivo para una sola
    #db o json
    def __init__(self,opt):
        #traerl el path del folder
        
        self.folder = os.path.join(os.getcwd(),'db')
        self.option = opt
        self.obj = NistApi()
    #esta funcion es la encargada de guardar los datos en los json, eta trae los path del folder  los json
    #no esta declarada ninguna validadcion asi que los json deben estar creados al igual que las
    #carpetas
    
    def createJson(self,data,name,start=0):
        #creacion la data a guardar
        item = {
            "old_start" : start,
            "time_save" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "amount" : self.obj.search_amount() ,
            "data" : data

        }
        data_json = self.path_db(nam=name)
        with open(data_json,'w') as db:
            json.dump(item,db,indent=2)
    #esta funcion trae el objeto como tal del archivo json
    def search_obj(self,name):      
        data_json = self.path_db(nam=name)
        with open(data_json,'r') as db:
            data = json.load(db)
            return data
    def path_db(self,nam):
        #-opcion 1 = guardar en las nulnerabilidades viejas
        #-opcion 2 = Nuevas vulnerabilidades
        #traer el path del json
        name = ""
        print(f'folder: {self.folder}')
        if self.option == 1:
            name = 'OldVulns.json'
        else: 
            name = nam
        data_json = os.path.join(self.folder,name)
        print(f"El nombre es: {data_json}")
        if os.path.exists(data_json):
             return data_json
        else:
            d = {
                "time_save": "2023-2-23 00:00:00",
            
            }
            with open(data_json,'w') as objson:
                json.dump(d,objson)
            return data_json
                
  


    
            

            


        