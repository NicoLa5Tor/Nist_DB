from .update_data import Update
from .elements.functionsOs import OperationOs
import json,time
class Search:
    obj_vulns = {}
    def __init__(self):
        self.update = Update()
        self.opOs = OperationOs(opt=2)
        self.none = self.low = self.medium = self.high = self.critical = self.awaitAnalisis = self.total =0
        self.dictio = {}
    def data_vulns(self):
        dt,lastElemnt =  self.update.concat_mayor()
        print(f"El elmento es {lastElemnt}")
        for i in range(lastElemnt): 
            db = f"NewVulns_{i+1}.json"
            self.concat_vulns(db=db)
        print("termina el proceso")
        return self.none,self.low,self.medium,self.high,self.critical,self.awaitAnalisis,self.total,self.dictio
        
    def concat_vulns(self,db):
       # print(f"db es: {db}")
            try:
                
                obj = self.opOs.search_obj(name=db)
                vulns =  obj['data']['vulns']
                for item in vulns:
                  #  print(item)
                  #contatenacion por mes
                    data_time = item['cve']['published']
                    anio,month,__ = data_time.split('-') 
                   # print("hizo el split")
                    
                    #print(month)
                   # time.sleep(3)
                    if anio not in self.dictio:
                        self.dictio[anio] = {str(month):1}
                    else:
                        if month not in self.dictio[anio]:   
                             self.dictio[anio][month] = 1 
                        else:
                            dat_in_month = self.dictio[anio][month]
                            self.dictio[anio][month] = (dat_in_month + 1)
                  #  print(json.dumps(self.dictio,indent=2))
                    #concatenacion de vulnerabilidades
                    if len(item['cve']['metrics']) < 1:
                        self.awaitAnalisis += 1
                    else:
                        if 'cvssMetricV31' in item['cve']['metrics']:
                            i = item['cve']['metrics']['cvssMetricV31'][0]['cvssData']['baseSeverity']
                        else :
                            i = item['cve']['metrics']['cvssMetricV30'][0]['cvssData']['baseSeverity']
                #     print(f'el item es {i}')
                        if i == 'MEDIUM':
                            self.medium += 1
                        elif i == 'HIGH':
                            self.high += 1
                        elif i == 'CRITICAL':
                            self.critical += 1
                        elif i == 'LOW':
                            self.low += 1
                        elif i == 'NONE':
                            self.none += 1
                    self.total += 1
            except Exception as e:
                print(f"Error al trarer el objeto de la base de 'datos' {e}")

