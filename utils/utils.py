import uuid
def get_random_string():
    return str(uuid.uuid4().hex)+'.csv'

def get_random_text():
    return str(uuid.uuid4().hex)

def replace_specific(actual_string,info,replacement_text):
    # if type(info) == "<class 'str'>":
    #     info = eval(info)
    info = eval(info)
    # print(type(info))
    # print(info['value'])
    # print(type(info['start_index']))
    
    value = info['value']
    if (value is None) or (info['start_index'] is None):
        return actual_string

    
    
    # print(value['start_index'],type(start_index))
    try:
        start_index = actual_string.index(value)
        end_index = info['end_index']
        print(actual_string[start_index: start_index + len(value)] ,value)
        if actual_string[start_index: start_index + len(value)] == value:
            print('OK')
            actual_string = actual_string[:start_index] + replacement_text + actual_string[start_index + len(value):]
            return actual_string
    except Exception as e:
        print('[-] Some Error Happen in Replace Specific Function',e)
        return actual_string
    
