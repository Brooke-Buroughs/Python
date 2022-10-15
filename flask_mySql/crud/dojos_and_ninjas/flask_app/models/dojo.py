from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data["updated_at"]
        self.ninjas=[]
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos;"
        results=connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos=[]
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    @classmethod    
    def get_one(cls, data):
        query="SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results=connectToMySQL('dojos_and_ninjas').query_db(query,data)
        dojo=cls(results[0])
        for ninja1 in results:
            ninja_data={
                "id":ninja1["ninjas.id"],
                "first_name":ninja1["first_name"],
                "last_name":ninja1["last_name"],
                "age":ninja1["age"],
                "created_at":ninja1["ninjas.created_at"],
                "updated_at":ninja1["ninjas.updated_at"],
                "dojo_id":ninja1["dojo_id"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
    @classmethod
    def save(cls, data):
        query="INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)