import json
import sys

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = key
        else:
            if type(inverse[val]) == 'str':
                inverse[val] = [inverse[val]]
                inverse[val].append(key)
    return inverse


errors = []

try:
    with open("c:\InProgress\input_data_file.json", "r") as read_file:
        data = json.load(read_file)
        
    try :
        notes = data['Notes']
        settings = data['Settings']
        fileSettings = settings[0]['sFile']
    except:
        errors.append('Somthing went wrong when trying to find a json field')
        
        
    try :
        fileSettings[0] = invert_dict(fileSettings[0])
    except:
        errors.append('Somthing went wrong when adding a new json field') 
        
    try:
        with open("c:\InProgress\output_data_file2.json", "w") as write_file:
            json.dump(data, write_file,indent=2)
    except:
        errors.append('Somthing went wrong trying to write the file out.')   
except:
    errors.append('Somthing went wrong opening the input file')  
    

if errors:
    raise Exception(errors)
    






