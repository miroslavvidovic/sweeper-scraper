import os
import dataset

from bs4 import BeautifulSoup
from datetime import datetime

projectdir = os.path.dirname(__file__)
datadir = os.path.join(projectdir, 'data')
files = os.listdir(datadir)

print(datadir)

def find_by_strong_item_name(itemName):
    item = "Unidentified"

    strong = soup.find_all(string=itemName)
    td = strong[0].findParent().findParent().findNextSibling()
    for item in list(td.children):
        item = str(item).strip()

    return (item)

def findByStrongItemName2(itemName):
    strong = soup.find_all(string=itemName)
    td = strong[1].findParent().findParent().findNextSibling()
    for item in list(td.children):
        item = str(item).strip()
        print (item)


def find_computer_name():
    """
    Parse computer name by finding the correct span

    :return: computer name
    :rtype: string
    """
    computer_name = soup.select_one('span',{"class":"bigt"})
    return computer_name.text


def find_local_user():
    """
    Parse local username by finding the correct span

    :return: local username
    :rtype: string
    """
    local_user = find_by_strong_item_name('Registered user:\xa0')
    return local_user
    

def find_operating_system():
    """
    Parse operating system name by calling find_by_strong_item_name

    :return: operating system
    :rtype: string
    """
    os = find_by_strong_item_name('Operating system:')
    return os


def find_operating_system_type():
    """
    Parse os type by calling find_by_strong_item_name function

    :return: operatyng system type (x86-based or 64-based)
    :rtype: string
    """
    pc_type = find_by_strong_item_name('Type:')
    os_type = pc_type.split()[0]
    return os_type

    
# TODO: extract only year, everything else is not relevant
def find_operating_system_install_date():
    """
    Parse system installation date by calling find_by_strong_item_name function

    :return: os install date
    :rtype: string
    """
    timestamp = find_by_strong_item_name('Install date:\xa0')
    return(timestamp)


def find_pc_manufacturer():
    """
    Parse pc manufacturer by calling find_by_strong_item_name function

    :return: pc manufacturer
    :rtype: string
    """

    manufacturer = find_by_strong_item_name('Manufacturer:')
    return manufacturer
    

def find_pc_model():
    """
    Parse pc model by calling find_by_strong_item_name function

    :return: pc model
    :rtype: string
    """

    manufacturer = find_by_strong_item_name('Model:')
    return manufacturer


def find_chassis_type():
    """
    Parse chassis type by calling find_by_strong_item_name function

    :return: chassis type (notebook, mini tower, desktop ...)
    :rtype: string
    """

    try:
        chassis = find_by_strong_item_name('Chassis:')
    except:
        chassis = "Unknown"

    return chassis.split('-')[0]

    
def find_cpu_name():
    """
    Parse cpu name type by calling find_by_strong_item_name function

    :return: cpu name
    :rtype: string
    """

    cpu = find_by_strong_item_name('Name:')
    return cpu 


def find_cpu_manufacturer():
    """Parse CPU manufacturer name

    Returns:
        string -- CPU manufacturer name
    """
    processor_table = soup.findAll('table')[8]
    content = processor_table.find_all(string="Manufacturer:\xa0")
    td = content[0].findParent().findParent().findNextSibling()
    for item in list(td.children):
        item = str(item).strip()

    return (item)


def find_total_ram_memory():
    """
    Parse amount of ram memory by calling find_by_strong_item_name function

    :return: total ram memory
    :rtype: string
    """

    ram = find_by_strong_item_name('Total memory:\xa0')
    return ram 


# TODO:Needs to be checked 
"List of GPUs"
def find_gpu_name():
    gpu_list = []

    gpu_table = soup.findAll('table')[10]
    content = gpu_table.find_all(string="Name:")
    for item in content:
        td = item.findParent().findParent().findNextSibling()
        if "DameWare" not in td.text:
            gpu_list.append(td.text)
    
    return gpu_list


def find_software():
    software = []

    soft_table = soup.find_all('table')[-2]

    data = soft_table.find_all('td',{"class":"stippel"})
    for element in data:
        # Remove trailing new lines
        filtered_element = element.text.rstrip()
        # Remove empty entries
        if filtered_element:
            software.append(filtered_element)
    
    return software


def print_all():
    print("------------------")
    print(find_computer_name())
    print(find_local_user())
    print(find_operating_system())
    print(find_operating_system_type())
    print(find_operating_system_install_date())
    print(find_pc_manufacturer())
    print(find_pc_model())
    print(find_chassis_type())
    print(find_cpu_name())
    print(find_cpu_manufacturer())
    print(find_gpu_name())
    print(find_total_ram_memory())
    print(find_software())

# def findTotalMemory():
#     findByStrongItemName('Total memory:\xa0')


for file in files:
    with open(os.path.join(datadir,file),"r") as f:
        page_content = f.read()

        soup = BeautifulSoup(page_content,'lxml')

        db = dataset.connect('mysql://admin:root@localhost/inventory')
        table = db['inventory']

        computername = find_computer_name()
        local_user = find_local_user()
        operating_system = find_operating_system()
        
        data = dict(computername=computername,local_user=local_user,operating_system=operating_system)
        # potreban upsert
        # table.insert(data, ['computername'])
        # insert radi

