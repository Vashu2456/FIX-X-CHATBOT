from pymongo import MongoClient

import config

anniedb = MongoClient(config.MONGO_URL)
annie = anniedb["FixxDb"]["Fixx"]


from .chats import *
from .users import *
