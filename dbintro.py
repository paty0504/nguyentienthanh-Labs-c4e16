from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds215739.mlab.com:15739/thanhdz1"

#1. connect to database
client = MongoClient(mongo_uri)

#2. get database
db = client.get_default_database()

#3. create collection
teencodes = db['teencodes']

#4. create a new document
# teencode = {"eny" : "Em người yêu",
# "any" : "Anh người yêu",
# "cl" : "con lợn",
# "hc" : "học",
# "ik" : "đi",
# "sml" : "sấp mặt luôn",
# "dc" : "được",
# "k" : "không",
#
# }

#5. insert document into collection
# teencodes.insert_one(teencode)

#read:
all_codes = teencodes.find()
for code in all_codes:
    print(teencodes)
