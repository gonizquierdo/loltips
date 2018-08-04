from db.DbFunctions import MongoConnector

client = MongoConnector('lol_stats_osg')
client.insert_one('test',{"TEST":"TEST"})