from .insert_data import AddVulns
obj = AddVulns(option=2)
if obj.insert_data() :
    print("Datos Guardados Exitosamente")
else:
    print("algo acurrió y no se guardó nada :(")
