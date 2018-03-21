from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
blog = db["posts"]
post = {
"title" : "Quick review :v",
"author" : "Thành không phải Ngưu ma vương",
"content" : "vote 5* luôn khỏi phải bàn cãi",}
blog.insert_one(post)
