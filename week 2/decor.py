import json
import yaml

def to_json(func):
    def json_dump(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return json_dump

def to_yaml(func):
    def yaml_dump(*args, **kwargs):
        return yaml.dump(func(*args, **kwargs))
    return yaml_dump

@to_json
def get_data():
    return{
        "data": 42
    }

@to_yaml
def get_data2():
    return{
        "data": 42
    }

print(get_data())
print(get_data2())
