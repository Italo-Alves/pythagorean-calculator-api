from flask import Flask, jsonify, request
import math
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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


app.run()
