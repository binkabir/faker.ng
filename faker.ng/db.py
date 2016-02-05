__author__ = 'ozo'

import pymongo


class DB(object):
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client.faker

    def find_people(self):
        people = self.db.find('people', {})
        people_json = map(lambda p: {
            "firstName": p["firstName"].encode("utf-8"),
            "lastName": p["lastName"].encode("utf-8"),
            "email": p["email"].encode("utf-8"),
            "phone": p["phone"].encode("utf-8"),
        }, people)

        return people_json
