import pymongo
from flask import current_app as app 

__author__ = 'ozo, shuaib, binkabir'


class DB(object):
    def __init__(self):

        server = app.config["DB_SERVER"]
        port   = app.config["DB_SERVER_PORT"]
        self.client = pymongo.MongoClient(server,port)
        self.db = self.client.faker

    def find_people(self):
        people = self.db.people2.find({})

        people_json = map(lambda p: {
            "firstName": p["first_name"].encode("utf-8"),
            "surname": p["surname"].encode("utf-8"),
            "email": p["email"].encode("utf-8"),
            "sex": p["sex"].encode("utf-8"),
            "mobile_number": p["mobile_number"].encode("utf-8"),
            "address": p["address"].encode("utf-8")
        }, people)

        return people_json

    def find_emails(self):
        emails = self.db.people.find({})

        emails_json = map(lambda p: {
            "email": p["email"].encode("utf-8")
        }, emails)

        return emails_json

    def save_people(self, data):
        self.db["people"].insert(data)
