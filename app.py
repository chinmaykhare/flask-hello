from flask import Flask,jsonify

app = Flask(__name__)

return_num=0


@app.route('/')
def index():
    global return_num
    num_now=return_num
    return_num=return_num+1

    return jsonify(number=num_now)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)