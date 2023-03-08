import uuid
def get_random_string():
    return str(uuid.uuid4().hex)+'.csv'

def get_random_text():
    return str(uuid.uuid4().hex)
