#!/usr/bin/env python3

import sys
import re
import subprocess

# Search for the presence of PATTERN within a LIST (lst) of strings.
def search(lst, pattern):
    index=0
    for item in lst:
        if item.find(pattern) > -1:
            return index
        index += 1
    return False
    
# 

# Feed this function a string and it will return space-separated words as a list
def clmns2list(line):
    notabs = re.sub(r' +', ' ', line)
    listvals = notabs.split()
    return listvals

# returns S.M.A.R.T attributes as key-value pairs. f.e. { 'Power_On_Hours' : '78' , ... }
def smart(drive):
    
    # Retrieve drive info
    p = subprocess.Popen(["/usr/sbin/smartctl","--all", drive], stdout=subprocess.PIPE)
    output, err = p.communicate()

    # Split string into list of lines
    output = output.decode("utf-8").split('\n')

    # Parse output for drive information
    key = []
    val = []
    beg2 = search(output, "INFORMATION SECTION") + 1
    end2 = search(output, "DATA SECTION") - 1
    rows2 = range(beg2,end2)
    for row in rows2:
        temp = re.sub(r' +', ' ', output[row])
        data2 = temp.split(":", 1)
        print(data2)
        key.append(data2[0])
        val.append(data2[1].lstrip())

    # Parse output for SMART Attributes
    beg = search(output,"ID#") + 1
    end = search(output,"SMART Error Log Version") - 1
    rows = range(beg,end)
    if beg  > 0:
    
        for row in rows:
            data = clmns2list(output[row])
            key.append(data[1])
            val.append(data[9])
        print(key)
        print(val)

    # Order parsed input into dictionary    
    zip(key,val)
    smartdata = dict(zip(key,val))
    index = smartdata.keys()
    print(index)
    print(smartdata)

    return smartdata






if __name__ == "__main__":
    drive = "/dev/sdb"
    drive_info = smart(sys.argv[1])
    drive_inf[""]
