import xml.etree.ElementTree as et
#加载读取xml文件, filename也可以是xml代码
tree = et.parse("to_edit.xml")
#得到他的根元素，然后开始遍历
root = tree.getroot()

for e in root.iter("Name"):
    print(e.text)

for stu in root.iter("Student"):
    name = stu.find("Name")

    if name != None:
        name.set('test',name.text * 2)

stu = root.find('Student')


#生成一个新的元素
e = et.Element('ADDer')
e.attrib = {'a':'b'}
e.text = '我加的'

stu.append(e)

#一定要把修改后的内容写入到文件中，否则修改无效
tree.write("to_edit.xml")