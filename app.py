from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import math

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify('Calculadora de Pitágoras API')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        values = request.get_json()
        value1 = values["cathutes1"]
        value2 = values["cathutes2"]
        if ',' in value1 or ',' in value2:
            value1 = value1.replace(',', '.')
            value2 = value2.replace(',', '.')
            hypotenuse = math.sqrt(
                math.pow(float(value1), 2) + math.pow(float(value2), 2))
            response = {
                "hypotenuse": float(("{:.3f}".format(hypotenuse))),
                "cathutes1": value1,
                "cathutes2": value2
            }
            return jsonify(response)

        else:
            hypotenuse = math.sqrt(
                math.pow(float(value1), 2) + math.pow(float(value2), 2))
            response = {
                "hypotenuse": float(("{:.3f}".format(hypotenuse))),
                "cathutes1": value1,
                "cathutes2": value2,
            }
            return jsonify(response)

    except Exception as e:
        return dict(error="Calculation Error", exception=str(e), message="Review all fields and try again"), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
