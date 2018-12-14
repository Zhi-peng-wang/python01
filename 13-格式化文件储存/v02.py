import xml.etree.ElementTree

#加载读取xml文件
root = xml.etree.ElementTree.parse("student.xml")
print("利用getiterator访问：")
#得到相应的可迭代的node集合
nodes = root.getiterator()
for node in nodes:
    #node.tag: node对应的tagename
    #node.text: node的文本值
    print("{0}--{1}".format(node.tag,node.text))


print("利用find和findall方法：")
#find(node_name):查找指定node_name的节点，返回一个node
ele_teacher = root.find("Teacher")
print(type(ele_teacher))
print("{0}--{1}".format(ele_teacher.tag,ele_teacher.text))

#root.findall(node_name):返回多个node_name节点
ele_stus = root.findall("Student")
print(type(ele_stus))
for ele in ele_stus:
    print("{0}--{1}".format(ele.tag,ele.text))
    for sub in ele.getiterator():
        if sub.tag == "Name":
            #node.attrib：node的属性的字典类型的内容
            if "Other" in sub.attrib.keys():
                print(sub.attrib['Other'])




