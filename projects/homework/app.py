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
    # POST API 설계
    #
    #   사용자 요청
    #       닉네임, 응원댓글 요청
    #       nickname_give, comment_give
    #   API 처리
    #       사용자 요청 값을 딕셔너리 형태로 데이터베이스에 저장
    #       데이터베이스 이름 : fan
    #   데이터 응답
    #       메시지 : 저장되었습니다!
    #       'msg' : '저장되었습니다!'

    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']

    doc = {
        'nickname': nickname_receive,
        'comment': comment_receive
    }
    db.fan.insert_one(doc)

    return jsonify({'result': 'success','msg':'저장되었습니다'})

@app.route("/fan/get", methods=["GET"])
def homework_get():
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)