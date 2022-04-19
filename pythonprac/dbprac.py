from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8yqbf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.nabacamp

doc = {
    'name': 'mary',
    'age': 24
}

db.users.insert_one(doc)