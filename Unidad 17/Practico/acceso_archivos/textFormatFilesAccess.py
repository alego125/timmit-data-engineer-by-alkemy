# Write
# with open("test.txt","w") as f:
#     f.write("test string")

# Read
# with open("test.txt","r") as f:
#     print(f.read())

# Read big files
# with open("test.txt","r") as f:
#     for line in f:
#         print(line)

# json

# Write
# import json

# test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
# json_str = json.dumps(test_dict,indent=4,sort_keys=True)

# with open('test.json',"w") as f:
#     f.write(json_str)

# Read
# import json

# with open('test.json',"r") as f:
#     json_dic = json.load(f)
#     print(json_dic["bigberg"])

# Read and Write CSV files

# Write
# import csv

# datas = [['name', 'age'],['Bob', 14], ['Tom', 23], ['Jerry', '18']]
# with open('example.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for row in datas:
#         writer.writerow(row)

# Read
# import csv
# with open("example.csv",'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(reader.line_num, row)

# Use class Dictwriter in CSV

# Write
# import csv

# headers = ['name', 'age']
# datas = [{'name': 'Bob', 'age': 23},
#          {'name': 'Jerry', 'age': 44},
#          {'name': 'Tom', 'age': 15}]

# with open('example.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, headers)
#     writer.writeheader()
#     for row in datas:
#         writer.writerow(row)

# Read
# import csv

# filename = 'example.csv'
# with open(filename) as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         name = row['name']
#         print(name)

# Read and write xml files

# Read
#coding=utf-8
# import xml.dom.minidom


# def GenerateXml():
#     impl = xml.dom.minidom.getDOMImplementation()
#     dom = impl.createDocument(None, 'CONFIG_LIST', None)
#     root = dom.documentElement
#     employee = dom.createElement('COMP')
#     root.appendChild(employee)
#     nameE = dom.createElement('path')
#     nameE.setAttribute ("valor", "aaaaaaaaaaa") # Agregar atributo
#     nameT = dom.createTextNode('linux')
#     nameE.appendChild(nameT)
#     employee.appendChild(nameE)
#     f = open('config_new.xml', 'a')
#     dom.writexml(f, addindent=' ', newl='\n')
#     f.close()


# GenerateXml()

# Read
import xml.etree.cElementTree as ET

tree = ET.parse("config_new.xml")
root = tree.getroot()
COMP = root.findall('COMP')[0]
print("Tag:", COMP.tag, "Attributes:", COMP.attrib, "Text:", COMP.text.strip(), "Tail:", COMP.tail)
ruta = COMP.findall("ruta")[0]
print("Tag:", path.tag, "Attributes:", path.attrib, "Text:", path.text.strip(), "Tail:", path.tail)
