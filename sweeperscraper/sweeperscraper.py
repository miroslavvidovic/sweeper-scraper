import os

from bs4 import BeautifulSoup

projectdir = os.path.dirname(__file__)
datadir = os.path.join(projectdir, 'data')
files = os.listdir(datadir)

print(datadir)

def findByStrongItemName(itemName):
    strong = soup.find_all(string=itemName)
    td = strong[0].findParent().findParent().findNextSibling()
    for item in list(td.children):
        item = str(item).strip()
        print (item)

def findByStrongItemName2(itemName):
    strong = soup.find_all(string=itemName)
    td = strong[1].findParent().findParent().findNextSibling()
    for item in list(td.children):
        item = str(item).strip()
        print (item)

def findOperatingSystem():
    findByStrongItemName('Operating system:')

"32 or 64 bit"
def findOperatingSystemType():
    findByStrongItemName('Type:')
    
"Install date"
def findOperatingSystemInstallDate():
    findByStrongItemName('Install date:\xa0')

"Install date"
def findManufacturer():
    findByStrongItemName('Manufacturer:')
    
"Model"
def findModel():
    findByStrongItemName('Model:')

"Cpu name"
def findCpuName():
    findByStrongItemName('Name:')

"Cpu manufacturer"
def findCpuManufacturer():
    #Manufacturer is the first element in cpu name .split[0]
    print()

"Cpu name"
def findGpuName():
    findByStrongItemName2('Name:')

def findTotalMemory():
    findByStrongItemName('Total memory:\xa0')

for file in files:
    print(file)
    with open(os.path.join(datadir,file),"r") as f:
        page_content = f.read()

        soup = BeautifulSoup(page_content,'lxml')

        findOperatingSystem()
        findOperatingSystemType()
        findOperatingSystemInstallDate()
        findManufacturer()
        findModel()
        findCpuName()
        #findCpuManufacturer()
        #findGpuName()
        findTotalMemory()



        #soup = BeautifulSoup(page_content,'lxml')
        #print (soup)