from db import DB
from parser import Parser


def save_people():
    parser = Parser()
    data = parser.parse()
    DB().save_people(data)


def find_people():
    people = DB().find_people()
    print people

save_people()
