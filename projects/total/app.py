from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8yqbf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.nabacamp

import requests
from bs4 import BeautifulSoup
###




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
###


# 나홀로피디아 페이지
@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route("/movie/post", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    # 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.

    # print(soup)

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title': title,
        'image': image,
        'desc': desc,
        'star': star_receive,
        'comment': comment_receive
    }
    db.metaMovie.insert_one(doc)

    return jsonify({'result':'success','msg':'DB 저장완료'})

@app.route("/movie/get", methods=["GET"])
def movie_get():
    # API 설계
    #
    #   사용자 요청
    #       없음
    #   API 처리
    #       모든 데이터베이스 찾기
    #   데이터 응답
    #       all_db: all_db

    all_db = list(db.metaMovie.find({},{'_id':False}))

    return jsonify({'result': 'success','all_db': all_db})
###


# 화성땅공동구매 페이지
@app.route('/mars')
def mars():
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
    # API 설계
    #
    #   사용자요청
    #       없음
    #   API 처리
    #       mars DB 데이터 전체 가져오기
    #   응답 데이터
    #       mars_data

    mars_data = list(db.mars.find({},{'_id':False}))

    return jsonify({'result': 'success', 'all_data': mars_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
