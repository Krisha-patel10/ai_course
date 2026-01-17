person = {
    "fname": "abc",
    "mname": "aaaa",
    "lname": "xyz",
   "parents":{
        "father": {
            "name": "aaaa"
        },
        "mother": {
            "name": "bbbb"
        }
         },
        "quali": ["ssc","hsc","BCA"],
        "hobbies": {},
        "isAlive": True    
}
print(person)
print(person["isAlive"])

person["isAlive"] = False
print(person["isAlive"])

print(type(person))