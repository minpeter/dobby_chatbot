import json
# from os import read


def readfile(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return ''

def readjson(filename):
    return json.loads(readfile(filename))

def read_school_info(key):
    try:
        data = readjson("school_info.json")
    except:
        print("school_info 파일이 json 형식인지 확인해주세요")
    try:
        if data[key] != "" or data[key] != None:
            return {key:data[key]}
        else:
            return {key:None}
    except:
        return {key:None}
    

def read_api_key(key):
    return readjson('api_key.json')[key]

def writefile(filename, data):
    try:
        with open(filename,'r+') as f:
            f.read()
            f.seek(0)
            f.write(data)
            f.truncate()
    except:
        return '오류발생'
    
def writejson(filename, data):
    writefile(filename, json.dumps(data))
    
def write_school_info(data):
    writejson('school_info.json', data)