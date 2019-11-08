import json
'''
here we read the data from json file. from wherever we need the data we are going
to import this method and pass the parameter and the data will be returned from 
the json file
'''

class read_json_data:

    def json_Reads(self, str):
        with open('data.json') as json_file:
            data = json.load(json_file)
            for p in data['paths']:
                pass
        return p[str]