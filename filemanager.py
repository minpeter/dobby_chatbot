import json
import os

# filemanager.py 파일이 위치한 디렉토리 경로를 반환합니다.
# filename 인자가 존재할경우 해당 파일의 경로를 반환합니다.
def file_dir(filename=""):
    return f"{os.path.dirname(os.path.realpath(__file__))}/{filename}"

def readfile(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return 'file read error ❌'

def prtBanner():
    print(readfile(file_dir("banner.txt")))

def readjson(filename):
    return json.loads(readfile(filename))

def read_school_info(key):
    try:
        data = readjson(file_dir("school_info.json"))
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
    return readjson(file_dir("api_key.json"))[key]

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
    writejson(file_dir("school_info.json"), data)

def read_quiz():
    return readjson(file_dir("quiz.json"))