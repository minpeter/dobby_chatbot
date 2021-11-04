import filemanager as fm

if fm.readfile("school_info.json") ==  "":
    print("File not found")
else:
    print(fm.readfile("school_info.json"))