from flask import Flask, render_template, jsonify
from google_sheets import get_all_machines, add_machine

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/machines')
def machines():
    data = get_all_machines()
    return jsonify(data)

@app.route('/add-machine', methods=['POST'])
def add_new_machine():
    # MODELO DE MAQUINA
    # ADICIONANDO MAQUINA EXEMPLO (MANUALMENTE)
    try:
        new_machine = {
            "operatingSystem": "Windows 10",
            "siteName": "Estação 1",
            "deviceType": "Desktop",
            "hostname": "station-001",
            "lastLoggedInUser": "user01",
            "online": "True"
        }
        add_machine(new_machine)
        return jsonify({"status": "Máquina adicionada com sucesso!"})
    except Exception as e:
        return jsonify({"status": e})

if __name__ == '__main__':
    app.run(debug=True)
