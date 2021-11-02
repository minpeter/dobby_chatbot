def readfile(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return ''
