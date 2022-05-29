import os
import string

def scan_disks():
    
    unitys = list()
    for drive in str(string.ascii_uppercase):
        if os.path.exists(f'{drive}:'):       
            unitys.append(f'{drive}:/') 
        else:
            pass

    for disk in unitys: 
        dir = disk
        items = list()
        unity = os.scandir(dir)
        for item in unity:
            items.append(item.name)
        if 'DATAP.HED' and 'DATAP.WAD' in items:
            return True, disk, unitys
            
    return False, unitys







    

        

            


