import pymongo
import app.utils.config as config

client = pymongo.MongoClient(config.get_database_server_url(), config.get_database_server_port())

db = client['pricing']

prices = db.prices

discounts = db.discounts
