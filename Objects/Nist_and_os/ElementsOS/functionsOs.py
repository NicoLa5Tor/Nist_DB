import os,json,datetime


class OperationOs:
    #la clase pide como unico dato opt con el fin de realizar un objeto exclusivo para una sola
    #db o json
    def __init__(self,opt):
        #traerl el path del folder
        
        self.folder = os.path.join(os.getcwd(),'DB')
        self.option = opt
    #esta funcion es la encargada de guardar los datos en los json, eta trae los path del folder  los json
    #no esta declarada ninguna validadcion asi que los json deben estar creados al igual que las
    #carpetas
    
    def createJson(self,data):
        #creacion la data a guardar
        item = {
            "time_save" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "data" : data
        }
        data_json = self.path_db()
        with open(data_json,'w') as db:
            json.dump(item,db,indent=2)
    def search_save_time(self):      
        data_json = self.path_db()
        with open(data_json,'r') as db:
            data = json.load(db)
            return data['time_save']
    def path_db(self):
        #-opcion 1 = guardar en las nulnerabilidades viejas
        #-opcion 2 = Nuevas vulnerabilidades
        #traer el path del json
        name = ""
        if self.option == 1:
            name = 'OldVulns.json'
        elif self.option == 2:
            name = 'NewVulns.json'
        data_json = os.path.join(self.folder,name)
        return data_json

    
            

            


        