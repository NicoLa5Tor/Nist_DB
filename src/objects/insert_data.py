from .elements.functionsOs import OperationOs
from .nist_api.api import NistApi
from datetime import datetime,timedelta
import asyncio
class AddVulns():
    def __init__(self,option):
        self.obj_os = OperationOs(opt=option)
        self.obj_nist = NistApi()
        self.opt = option
    def save_or_not(self):
        #se obtiene el dato save time donrrespondiente a la fecha de guardado de la informcion
        time_save_string = self.obj_os.search_save_time()
        time_save = datetime.strptime(time_save_string,"%Y-%m-%d %H:%M:%S")
        time_actual = datetime.now()
        dif_time = time_actual - time_save
        #print(dif_time)
        d_20 = timedelta(days=20)
        #valida si la resta entre ambas fechas es mayor a la fecha actual, de ser asi,
        #arrojará true, de no ser arrojará falso
        if dif_time > d_20:
            return True
        else:
            return False 
    async def insert_data(self,start_index,number=0,amount = None):
                st = int(start_index)
                if amount is not None:
                     amo = int(amount)
                     max_amount = (amo / 1000)*1000  
                else:
                    max_amount = (await self.obj_nist.search_amount() / 1000)*1000   
                cont = 1  

                while True:
                    nam = ""
                    if number > 0:
                        nam = f"NewVulns_{number}.json"
                        number += 1
                    else:
                        nam = f"NewVulns_{cont}.json"
                    print(f"El nombre es {nam}")
                    print(f"start del insert: {st}")
                    data,start = await self.obj_nist.search_vulnerabilities(start=st)
                    print(f"start: {start}")
                    if data is not None:
                        self.obj_os.createJson(data=data,name=nam,start=st)
                    st = start   
                    
                    print(f"amount comparado en el insert: {max_amount}")
                    if start >= max_amount:
                           print("retorna verdadero en el insert")
                           return True
                    cont += 1
                    print(f"termina el ciclo {cont}")
             
                    
        

       





    


    
    


