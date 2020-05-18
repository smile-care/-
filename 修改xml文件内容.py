# coding=utf-8
import os
import os.path
import xml.dom.minidom

#获得文件夹中所有文件
FindPath = 'G:\研究生文件夹（深大）\机器学习\磁瓦\磁瓦(标注数据)\dataset/annotation - 副本/'    
FileNames = os.listdir(FindPath)
s = []
xml_path = 'G:\研究生文件夹（深大）\机器学习\磁瓦\磁瓦(标注数据)\dataset/annotation - 副本/'
for file_name in FileNames:
    if not os.path.isdir(file_name):  # 判断是否是文件夹,不是文件夹才打开
        print(file_name)

    #读取xml文件
    dom = xml.dom.minidom.parse(os.path.join(FindPath,file_name))

    root = dom.documentElement

    # 获取标签对name之间的值
    name = root.getElementsByTagName('name')
    for i in range(len(name)):
        print (name[i].firstChild.data)
        #if name[i] .firstChild.data== 'screw cap':
        if name[i].firstChild.data == 'bad chamfer':
            name[i].firstChild.data = 'djbl'
        # name[i].firstChild.data = 'hand'
        print ('修改后的 name')
        print (name[i].firstChild.data)
    #将修改后的xml文件保存
    with open(os.path.join(xml_path, file_name), 'w') as fh:
        dom.writexml(fh)
        print('写入name/pose OK!')
        print('\n')
