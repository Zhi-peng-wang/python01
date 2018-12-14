import json


data = {"name":"hahah", "age":12}


with open("t.json", 'w') as f:
    #json.dump(): 把内容写入文件
    json.dump(data, f)


with open("t.json", 'r') as f:
    #json.load(): 把json文件内容读入python
    d = json.load( f)
    print(d)