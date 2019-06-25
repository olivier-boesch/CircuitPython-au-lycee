import re
def board_info():
    with open('boot_out.txt','r') as f:
        data = f.read()
    regexstr = r'([a-zA-Z0-9]* [a-zA-Z0-9]*) (.*) on (.*); (.*) with ([a-zA-Z0-9]*)'
    res = re.match(regexstr,data)
    retval = {'firmware' : res.group(1),
              'firmware_version' : res.group(2),
              'firmware_date' : res.group(3),
              'board_type' : res.group(4),
              'mcu' : res.group(5)}
    return retval
    
