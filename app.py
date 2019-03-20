from flask import Flask, jsonify
import os, copy


app = Flask(__name__)

person1 = {
    "id": 1,
    "first_name":"Sean",
    "last_name": "Warfman",
    "age":25,
    "parents":[3,4],
    "kid":[]
}

person2 = {
    "id": 2,
    "first_name":"Casey",
    "last_name": "Warfman",
    "age":30,
    "parents":[3,4],
    "kid":[]
}

person3 = {
    "id": 3,
    "first_name":"Lynette",
    "last_name": "Lindahl",
    "age":58,
    "parents":[7,8],
    "kid":[]
}

person4 = {
    "id": 4,
    "first_name":"Scott",
    "last_name": "Warfman",
    "age": 61,
    "parents":[7,8],
    "kid":[]
}

person5 = {
    "id": 5,
    "first_name":"Richard",
    "last_name": "Lindahl",
    "age": 82,
    "kid":[3],
    "parents":[]
}

person6 = {
    "id": 6,
    "first_name":"Joan",
    "last_name": "Heron",
    "age": 80,
    "kid":[3],
    "parents":[]
}

person7 = {
    "id": 7,
    "first_name":"Mortimer",
    "last_name": "Warfman",
    "age": 70,
    "kid":[4],
    "parents":[]
}

person8 = {
    "id": 8,
    "first_name":"Sheila",
    "last_name": "Warfman",
    "age": 70,
    "kid":[4],
    "parents":[]
}

family={
    "members":[person5, person6, person7, person8, person4, person3, person2, person1]
}

def getElement(a):
    for i in family["members"]:
        if a == i["id"]:
            return i


@app.route('/')
def index():
    return jsonify(family)

@app.route('/member/<int:id>')
def get_member(id):
    if id > 0:
        print(family["members"])
        for i in family["members"]:
            if id == i["id"]:
                ele = copy.deepcopy(i)
                print(ele)
                x = ele["parents"]
                tempList = []
                for n in x:
                    tempList.append(getElement(n))
                ele["parents"] = tempList
                     
                
                return jsonify({"status_code": 200, "data": ele})
    
            
        response = jsonify({"error": 400, "message":"no member found" })
        response.status_code = 400
        return response



app.run(host='0.0.0.0', port=os.environ.get('PORT'))