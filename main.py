from src.objects.insert_data import AddVulns
from flask import Flask,jsonify,request,render_template,render_template_string
from src.objects.update_data import Update 
import threading,asyncio,time,json
#con esta libreria creamos el pool de hilos
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
obj_insert  = AddVulns(option=2)
dicc = None
#creamos solo dos hilos, para se ejecutados
json_data = {"response":"Actualizacion en proceso"}
@app.route('/save_data')
def nist():
    start = request.args.get('start_index')
    try: 
        save = obj_insert.insert_data(start_index=start)
        if save:
            return jsonify({
                "response" : "datos almacenados",
                "status" : 200
            })
        else:
            return jsonify({
                "resposne" : "error al guardar datos",
                "status" : 403
            })
    except Exception as e:
        print(f"Error al retornar el valor en la funcion main: {e}")
        return jsonify({
            "data" : None,
            "status" : 500
        })
@app.route('/update_data')
def update_thread(val = None):
   global json_data
   global thread_up 
   if val is None:
        print("ejecuta el hilo")
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(run_update)
   else:
       
       json_data = val
       
       
   with app.app_context():
     return jsonify(json_data)  
        
 
async def update():
    try:
      
        obj = Update()
        dt = await obj.update_data()
        response = {
            "response" : dt,
            "status": 200
        }
        print(f"retorna {dt}")
        print("si hace todo el proceso, deberia retornar el response")
    except Exception as e:
        response = {
            "response":str(e),
            "status":"error"
        }
    finally:
        return  response
                          
def run_update():
   dat =  asyncio.run(update())
   update_thread(dat)
    


#descomentar en uso local
#comj
if __name__ == '__main__':
    app.run(debug=True,port=4000)