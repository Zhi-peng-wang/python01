
import json

# 此时student是一个python中字典dict格式内容，不是json
student={
    "name": "luidana",
    "age": 18,
    "mobile":"15578875040"
}

print(type(student))
#json.dumps():对数据编码，把python格式表示成json格式
stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象:{0}".format(stu_json))

#json.loads(): 对数据解码，把json格式转换成python格式
stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)