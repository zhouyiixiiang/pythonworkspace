import xml.dom.minidom
#创建一个空的文档
doc=xml.dom.minidom.Document()
#创建一个根节点Managers对象
root=doc.createElement("Managers")
#设置根节点属性
root.setAttribute('company','CASIT')
root.setAttribute('address','Chengdu Branch, Chinise academy of sciences')
#将节点添加到文档对象中
doc.appendChild(root)

manageList=[{'name':'a','age':'27','sex':'女'},
			 {'name':'b','age':'22','sex':'女'},
			 {'name':'c','age':'21','sex':'男'},
			 {'name':'d','age':'23','sex':'女'},
			 {'name':'e','age':'24','sex':'女'},
			 {'name':'f','age':'25','sex':'男'}]

for i in manageList:
	nodeManager=doc.createElement('Manager')
	nodeName=doc.createElement('name')
	#给叶节点name设置一个文本节点，用于显示文本内容
	nodeName.appendChild(doc.createTextNode(str(i['name'])))
	nodeAge = doc.createElement("age")
	nodeAge.appendChild(doc.createTextNode(str(i["age"])))
	nodeSex = doc.createElement("sex")
	nodeSex.appendChild(doc.createTextNode(str(i["sex"])))
	#将各叶子节点添加到父节点Manager中，
	#最后将Manager添加到根节点Managers中
	nodeManager.appendChild(nodeName)
	nodeManager.appendChild(nodeAge)
	nodeManager.appendChild(nodeSex)
	root.appendChild(nodeManager)

	
#开始写xml文档
fp = open('.\Manager.xml', 'w')
doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")