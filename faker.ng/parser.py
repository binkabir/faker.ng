import json
__author__ = 'ozo'


class Parser(object):
    def __init__(self):
        # TODO - The path needs to be externalised
        self.path = '/Users/ozo/iworkspace/faker.ng/faker.ng/sample-data.json'

    def parse(self):
        file = open(self.path, 'r')
        for line in file:
            print(line)

parser = Parser()
parser.parse()
