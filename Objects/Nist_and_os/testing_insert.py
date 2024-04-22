from insert_data import AddVulns
obj = AddVulns(option=1)
if obj.insert_data() :
    print("Datos Guardados Exitosamente")
else:
    print("algo acurrió y no se guardó nada :(")
