import xml.dom.minidom
#负责解析xml文件
from xml.dom.minidom import parse

#使用mindom打开xml文件
#加载读取xml文件, filename也可以是xml代码
DOMTree = xml.dom.minidom.parse("student.xml")
#获取xml文档对象，一个xml文件只有一个对于的文档对象
doc = DOMTree.doucumentElement

#显示子元素
for ele in doc.childNodes:
    if ele.nodeName == "Teacher":
        print("------Node:{0}-----".format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == "Name":
                #data是文本节点的一个属性，表示他的值
                print("Name:{0}".format(child.childNodes[0].data))
            if child.nodeName == "Mobile":
                # data是文本节点的一个属性，表示他的值
                print("Mobile: {0}".format(child.childNodes[0].data))
            if child.nodeName == "Age":
                # data是文本节点的一个属性，表示他的值
                print("Age: {0}".format(child.childNodes[0].data))
                if child.hasAttribute("detail"):
                    print("Age-deetail:{0}".format(child.getAttribute("detail")))
