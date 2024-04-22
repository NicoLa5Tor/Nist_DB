from flask import Flask,jsonify,request,render_template
from Objects.Nist.api import NistApi


app = Flask(__name__)
obj = NistApi()
@app.route('/list')
def nist():
    try: 
        data = obj.nist()
        return jsonify({
            "data" : data,
            "status" : 200
        })
    except Exception as e:
        print(f"Error al retornar el valor en la funcion main: {e}")
        return jsonify({
            "data" : None,
            "status" : 500
        })
        
    
if __name__ == '__main__':
    app.run(debug=True)