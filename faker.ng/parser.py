import json
__author__ = 'ozo'


class Parser(object):
    def __init__(self):
        # TODO - The path needs to be externalised
        self.path = '/Users/ozo/iworkspace/faker.ng/faker.ng/sample-data.json'

    def parse(self):
        file = open(self.path, 'r')
        json_ouput = map(lambda line: json.loads(line), file)
        print json_ouput

parser = Parser()
parser.parse()
