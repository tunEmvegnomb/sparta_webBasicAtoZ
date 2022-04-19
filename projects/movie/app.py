from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8yqbf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.nabacamp

@app.route('/movie')
def home():
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
        'desc': desc
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

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)