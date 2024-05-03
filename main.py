from src.objects.insert_data import AddVulns
from flask import Flask,jsonify,request,redirect
from src.objects.update_data import Update 
import threading,asyncio,time,json
from concurrent.futures import ProcessPoolExecutor

app = Flask(__name__)
obj_insert  = AddVulns(option=2)
executor = ProcessPoolExecutor(max_workers=1)
dicc = None
json_data = {"response":"Tarea completeda, para un mejor resultado vuelva a conusltar en 5 segundos"}
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
def update_thread():
   global json_data
   global thread_up 
   thread_up = threading.Thread(target=run_update)
   thread_up.start()
   return jsonify(json_data)
@app.route('/update_data_response')
def redict():
    response = request.args.get('response')
    return jsonify(response)          

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
   print(f"la respuesta es: {dat}")
   redirect(f'/update_data_response?response={dat}')
    


#descomentar en uso local
#comj
if __name__ == '__main__':
    app.run(debug=True,port=4000)