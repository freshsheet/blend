from flask import jsonify, Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({"id": "helloworld"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='4050')