import json
import os

resources = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schema'))


def load_schema(filename):
    with open(os.path.join(resources, filename)) as file:
        schema = json.load(file)
        return schema
