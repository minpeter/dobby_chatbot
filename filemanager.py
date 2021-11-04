import json
# from os import read


def readfile(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return ''

def readjson(filename):
    try:
        with open(filename, 'r') as f:
            return json.loads(f.read())
    except:
        return ''

def read_school_info():
    return readjson('school_info.json')

def writefile(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
    except:
        return ''
    
def writejson(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(json.dumps(data))
    except:
        return ''
    
def write_school_info(data):
    writejson('school_info.json', data)