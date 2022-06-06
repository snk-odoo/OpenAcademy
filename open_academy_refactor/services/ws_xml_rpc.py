import xmlrpc.client

url = "http://localhost:8569"
db = "o15-learn"
username = "service"
password = "service"
uid = None

def Login(url, db, username, password):
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    version = common.version()
    print("Details: ", version['server_version'])

    uid = common.authenticate(db, username, password, {})
    if uid != False:
        print("User ID: ", uid)

    return uid


def Test(url, db, password, uid):
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 3, 'limit': 4})
    print("Partners: ", partners)

    partner_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[]])
    print("Partner Count:", partner_count)

    partner_records_v1 = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners])

    for partner in partner_records_v1:
        print(partner['name'])
        pass
    #print("Partner records: ", partner_records)

    partner_records_name = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners], {'fields': ['id', 'name']})

    for partner in partner_records_name:
        print(partner)
        pass

    partner_records_v2 = models.execute_kw(db, uid, password, 'res.partner', 'search_read',
                                           [[['is_company', '=', True]]],
                                           {'fields': ['name', 'country_id', 'comment'], 'limit': 5})

    for partner in partner_records_v2:
        print(partner)
        pass

    new_id = models.execute_kw(db, uid, password, 'res.partner', 'create',
                           [{'name': "Test Corporation",
                             'company_type': "company"}])
    print("New partner id: ", new_id)

    pass


def Exercise(url, db, password, uid):
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    sessions = models.execute_kw(db, uid, password,
                                 'open_academy.session', 'search_read', [[]], {'fields': ['name', 'seats']})

    print("Sessions")
    print("Name", " - ", "Seats")
    for session in sessions:
        print(session['name'], " - ", session['seats'])
        pass

    record = {
        'name': "C++ for Advanced",
        'course_id': 4,
        'instructor_id': 35,
        'seats': 15,
        'duration': 2,
        'attendees_list': [35]
    }

    new_id = models.execute_kw(db, uid, password, 'open_academy.session', 'create', [record])
    print("New session id: ", new_id)

    pass


uid = Login(url, db, username, password)
if uid != False:
    Exercise(url, db, password, uid)
    pass
