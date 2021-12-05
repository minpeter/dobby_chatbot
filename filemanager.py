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

def readjson(filename):
    return json.loads(readfile(filename))

def read_api_key(key):
    return readjson(file_dir("api_key.json"))[key]

def prtBanner():
    print(readfile(file_dir("banner.txt")))

def read_quiz():
    return readjson(file_dir("quiz.json"))