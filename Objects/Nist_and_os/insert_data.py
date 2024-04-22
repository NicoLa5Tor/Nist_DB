from ElementsOS.functionsOs import OperationOs
from Nist_api.api import NistApi
from datetime import datetime,timedelta
import json
class AddVulns():
    def __init__(self,option):
        self.obj_os = OperationOs(opt=option)
        self.obj_nist = NistApi()
        self.opt = option
    def save_or_not(self):
        #se obtiene el dato save time donrrespondiente a la fecha de guardado de la informcion
        time_save_string = self.obj_os.search_save_time()
        #se convierte el string en datetime para porde rprocesarla con la otra fecha
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
    def insert_data(self):
        if self.save_or_not():
            if self.opt == 1:
                data = self.obj_nist.search_vulnerabilities(cont=220000)
                if data is not None:
                    self.obj_os.createJson(data=data)
                    return True
                else:
                    return False
        else:
            return False

       





    


    
    


