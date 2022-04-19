from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8yqbf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

@app.route('/mars')
def home():
    return render_template('mars.html')


@app.route("/mars/post", methods=["POST"])
def web_mars_post():
    # API 설계
    #
    #   사용자 요청
    #       이름, 주소, 평수 데이터
    #       name, address, size give
    #   API 처리
    #       받아온 사용자 요청값을 딕셔너리로 변수 지정정    #       데이터베이스에 저장
    #   응답 데이터
    #       주문이 완료되었습니다! 메시지 리턴
    #       'result': 'success', 'msg': '주문이 완료되었습니다'
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    print('사용자 요청값 확인: ', name_receive, address_receive, size_receive)

    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    db.mars.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다'})


@app.route("/mars/get", methods=["GET"])
def web_mars_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
