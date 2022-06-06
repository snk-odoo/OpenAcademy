import json
import random
import urllib.request

host = "localhost"
port = 8569
db = "o15-learn"
username = "service"
password = "service"
uid = None


def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    request = urllib.request.Request(url = url, data = json.dumps(data).encode(), headers={
        "Content-Type": "application/json",
    })
    reply = json.loads(urllib.request.urlopen(request).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]


def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

def get_url(host, port):
    return "http://%s:%s/jsonrpc" % (host, port)

def Login(url, db, username, password):
    uid = call(url, "common", "login", db, username, password)

    if uid != False:
        print("User ID: ", uid)

    return uid

def Exercise(url, db, password, uid):
    session_ids = call(url, "object", "execute", db, uid, password, 'open_academy.session', 'search', [])

    sessions = call(url, "object", "execute", db, uid, password, 'open_academy.session', 'read', session_ids)

    print("Sessions")
    print("Name", " - ", "Seats")
    for session in sessions:
        print(session['name'], " - ", session['seats'])
        pass

    record = {
        'name': "Pascal for Advanced",
        'course_id': 2,
        'instructor_id': 34,
        'seats': 25,
        'duration': 4,
        'attendees_list': [34]
    }

    new_id = call(url, "object", "execute", db, uid, password, 'open_academy.session', 'create', record)
    print("New session id: ", new_id)

    pass


url = get_url(host, port)

uid = Login(url, db, username, password)
if uid != False:
    Exercise(url, db, password, uid)
    pass

