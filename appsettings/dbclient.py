from pymongo import MongoClient
import os
import json
from appsettings import Settings


class DbClient:

    def __init__(self):
        settings = Settings()
        self.host = settings.get('mongo_host')
        self.port = settings.get('mongo_port')

        uri = "mongodb://%s:%s" % (self.host, self.port)
        self.client = MongoClient(uri)

        self.db = self.client[settings.get('mongo_db')]
        self.data = self.db[settings.get('mongo_data')]
        self.graph = self.db[settings.get('mongo_graph')]
        self.mrr = self.db[settings.get('mongo_mrr')]

        return

    def close(self):
        self.mrr = None
        self.graph = None
        self.data = None
        self.db = None
        self.client.close()
        return
