import os,json
from .nist_api.api import NistApi
from .elements.functionsOs import OperationOs
from .insert_data import AddVulns
import asyncio

class Update:
    def __init__(self):
        self.folder = os.path.join(os.getcwd(),'db')
        self.apiNist = NistApi()
        self.apiOs = OperationOs(opt=2)
        self.insert = AddVulns(option=2)
       
    def concat_mayor(self):
        def  _agroup_json():
            list_json = [arch for arch in os.listdir(self.folder) if arch.endswith(".json")]
            return list_json
        def _search_mayor():
            mayor = 0
            for item in _agroup_json():
                n,i = item.split('_')
                data,nn = i.split('.')
                dat = int(data)
                if dat > mayor:
                    mayor = dat
            return mayor
        intial = "NewVulns_"
        tam = _search_mayor()
        final = intial+str(tam)+".json"
        return final,tam
   
    def update_data(self):
        data,tam = self.concat_mayor()
        object_data = self.apiOs.search_obj(name=data)
        amount_neutral = object_data['amount']
        nistAmount = asyncio.run(self.apiNist.search_amount())
        if amount_neutral < nistAmount:
            self.insert.insert_data(number=tam,start_index=object_data['old_start'],amount=nistAmount)
            return "Datos Actualizados con exito"
        else:
            return "No hay actualizaciones"


    

            





        
