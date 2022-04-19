from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8yqbf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.nabacamp

# 퀴즈1. 영화제목 '가버나움' 평점을 가져오기
find = db.movies.find_one({'title':'가버나움'},{'_id':False})
# print(find)

# 퀴즈2. '가버나움'의 평점과 같은 영화 제목들을 가져오기
findT = list(db.movies.find({'star':find['star']},{'_id':False}))
for t in findT:
    print(t['title'])

# 퀴즈3. '가버나움' 영화의 평점을 문자열 0으로 만들기
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})
print('update star')

