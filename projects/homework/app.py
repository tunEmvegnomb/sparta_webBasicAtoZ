from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8yqbf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.nabacamp

@app.route('/fan')
def home():
    return render_template('fan.html')

@app.route("/fan/post", methods=["POST"])
def homework_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/fan/get", methods=["GET"])
def homework_get():
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)