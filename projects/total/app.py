from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8yqbf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.nabacamp

# 메인 페이지 렌더링
@app.route('/')
def main():
    return render_template('index.html')
###


# 버킷리스트 페이지
@app.route('/bucket')
def bucket():
    return render_template('bucket.html')

@app.route("/bucket/post", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.bucket.find({},{'_id':False}))
    count = len(bucket_list) + 1

    doc ={
        'num':count,
        'bucket': bucket_receive,
        'done': 0
    }
    db.bucket.insert_one(doc)
    return jsonify({'result': 'success','msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)},{'$set':{'done':1}})
    return jsonify({'msg': '버킷 완료!'})

@app.route("/bucket/get", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({},{'_id':False}))

    return jsonify({'result':'success','bucket_list':bucket_list})
###


# 팬명록 페이지
@app.route('/fan')
def fan():
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
    # GET API 설계
    #
    #   사용자 요청
    #       없음
    #   API 처리
    #       모든 데이터 불러오기
    #       all_data
    #   데이터 응답
    #       'all_data': all_data

    all_data = list(db.fan.find({},{'_id':False}))

    return jsonify({'result': 'success', 'all_data': all_data})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
