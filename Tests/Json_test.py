from App import App_Variable
import json
obj= App_Variable.Variables()
#print (obj.__dict__)

def jdefault(o):
    return o.__dict__
print(json.dumps(obj, default=jdefault))
#json.dumps(obj)