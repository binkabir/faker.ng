import pymongo

__author__ = 'ozo'


class DB(object):
    def __init__(self):
        # TODO - db server details needs to be externalised
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client.faker

    def find_people(self):
        people = self.db.find("people", {})
        people_json = map(lambda p: {
            "firstName": p["first_name"].encode("utf-8"),
            "surname": p["surname"].encode("utf-8"),
            "email": p["email"].encode("utf-8"),
            "phone": p["phone"].encode("utf-8"),
        }, people)

        return people_json

    def save_people(self, data):
        self.db["people"].insert(data)
