import pymongo

url='mongodb+srv://skybaseoOuth:rootDev@cluster0.y25uvyr.mongodb.net/'
client = pymongo.MongoClient(url)

db = client['django_stockmarket']