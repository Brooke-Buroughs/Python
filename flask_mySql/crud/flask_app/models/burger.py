from flask_app.config.mysqlconnection import connectToMySQL
# burger.py
class Burger:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# burger.py...
# gets all the burgers and returns them in a list of burger objects .
@classmethod
def get_all(cls):
    query = "SELECT * FROM burgers"
    burgers_from_db = connectToMySQL('burgers').query_db(query)
    burgers = []
    for b in burgers_from_db:
        burgers.append(cls(b))
    return burgers

# burger.py...
# gets all the burgers and returns them in a list of burger objects .
@classmethod
def save(cls,data):
    query = "Insert INTO burgers (name,bun,meat,calories,created_at,updated_at) VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW());"
    burger_id = connectToMySQL('burgers').query_db(query,data)
    return burger_id

