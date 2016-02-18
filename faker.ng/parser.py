import json
__author__ = 'ozo'

from index import PROJECT_PATH

class Parser(object):
    def __init__(self):
        # TODO - The path needs to be externalised
        self.path = PROJECT_PATH + 'sample-data.json'

    def parse(self):
        file = open(self.path, 'r')
        json_output = map(lambda line: json.loads(line), file)
        return json_output
