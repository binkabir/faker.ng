import pymongo

__author__ = 'ozo, shuaib'


class DB(object):
    def __init__(self):
        # TODO - db server details needs to be externalised
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client.faker

    def find_people(self):
        people = self.db.people.find({})

        people_json = map(lambda p: {
            "firstName": p["first_name"].encode("utf-8"),
            "surname": p["surname"].encode("utf-8"),
            "email": p["email"].encode("utf-8")
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
