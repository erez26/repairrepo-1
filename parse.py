import csv, json, pymongo
from pymongo import MongoClient

txtfile = open('small.txt', 'r') #txt file with subset of sample data

reader = csv.DictReader(txtfile, delimiter = '\t')

connection = MongoClient('mongodb://yasgari:701415@sancarlabdb-shard-00-00-v0rht.mongodb.net:27017,sancarlabdb-shard-00-01-v0rht.mongodb.net:27017,sancarlabdb-shard-00-02-v0rht.mongodb.net:27017/sampleResultsDb?ssl=true&replicaSet=SancarLabDB-shard-0&authSource=admin')
db = connection.sampleResultsDb
collection = db['sample']

for row in reader:
    collection.insert({'human':json.dumps(row)})

connection.close()
