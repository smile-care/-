import os
import xml.etree.ElementTree as ET

dirpath = 'G:/研究生文件夹（深大）/机器学习/磁瓦/磁瓦(标注数据)/dataset/annotation/'  # 原来存放xml文件的目录
newdir = 'G:/PyTorch-YOLOv3-master/data/labels/'  # 修改label后形成的txt目录


if not os.path.exists(newdir):
    os.makedirs(newdir)

for fp in os.listdir(dirpath):

    root = ET.parse(os.path.join(dirpath, fp)).getroot()

    xmin, ymin, xmax, ymax = 0, 0, 0, 0
    sz = root.find('size')
    width = float(sz[0].text)
    height = float(sz[1].text)
    filename = root.find('filename').text

    for child in root.findall('object'):  # 找到图片中的所有框

        sub = child.find('bndbox')  # 找到框的标注值并进行读取
        xmin = float(sub[0].text)
        ymin = float(sub[1].text)
        xmax = float(sub[2].text)
        ymax = float(sub[3].text)
        try:  # 转换成yolov3的标签格式，需要归一化到（0-1）的范围内
            x_center = (xmin + xmax) / (2 * width)
            y_center = (ymin + ymax) / (2 * height)
            w = (xmax - xmin) / width
            h = (ymax - ymin) / height
        except ZeroDivisionError:
            print(filename, '的 width有问题')

        with open(os.path.join(newdir, fp.split('.')[0] + '.txt'), 'a+') as f:
            f.write(' '.join([str('error'), str(x_center), str(y_center), str(w), str(h) + '\n']))

