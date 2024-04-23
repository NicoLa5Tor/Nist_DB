from flask import Flask,jsonify,request,render_template
from Objects.Nist_and_os.Nist_api.api import NistApi
from Objects.Nist_and_os.insert_data import OperationOs

app = Flask(__name__)
obj = NistApi()
obj_insert  = OperationOs(opt=2)
@app.route('/save_data')
def nist():
    try: 
        save = obj_insert.createJson()
        if save:
            jsonify({
                "response" : "datos almacenados",
                "status" : 200
            })
        else:
            jsonify({
                "resposne" : "error al guardar datos",
                "status" : 403
            })
    except Exception as e:
        print(f"Error al retornar el valor en la funcion main: {e}")
        return jsonify({
            "data" : None,
            "status" : 500
        })
        
    
if __name__ == '__main__':
    app.run(debug=True)