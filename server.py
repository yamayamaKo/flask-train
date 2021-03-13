from flask import Flask 
from flask import request, make_response, jsonify, render_template
from flask_cors import CORS
from utils import wakati

app = Flask(__name__, static_folder='./build/static', template_folder='./build')
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')
    # return "text parse:)"

@app.route("/wakati", methods=['GET', 'POST'])
def parse():
    print('テスト')
    data = request.get_json()
    text = data['post_text']

    # この辺で処理をする

    res = wakati(text)
    response = {'result':res}
    print(response)
    return make_response(jsonify(response))

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)