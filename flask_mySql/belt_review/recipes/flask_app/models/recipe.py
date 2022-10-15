from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash 
import re 

class Recipe:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instruction=data['instruction']
        self.date=data['date']
        self.time=data['time']
        self.user_id=data['user_id']
        self.user=None
    @classmethod
    def save(cls,data):
        query="INSERT INTO recipes (name, description, instruction, date, time, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(date)s, %(time)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL('recipes').query_db(query,data)
    @classmethod
    def get_all(cls):
        query="SELECT * FROM recipes JOIN users ON users.id=recipes.user_id;"
        results=connectToMySQL('recipes').query_db(query)
        recipes=[]
        for recipe1 in results:
            recipe=cls(recipe1)
            user_data={
                "id":recipe1["users.id"],
                "first_name":recipe1["first_name"],
                "last_name":recipe1["last_name"],
                "email":recipe1["email"],
                "password":recipe1["password"],
                "created_at":recipe1["users.created_at"],
                "updated_at":recipe1["users.updated_at"]
            }
            recipe.user=(user.User(user_data))
            recipes.append(recipe)
        return recipes
    @classmethod
    def get_recipe_by_user(cls, data):
        query="""
        SELECT * 
        FROM recipes  
        JOIN users 
        ON users.id=recipes.user_id
        WHERE recipes.id=%(id)s
        ;"""
        results=connectToMySQL('recipes').query_db(query, data)
        print("results",results)
        one_recipe=cls(results[0])
        user_data={
            "id":results[0]["users.id"],
            "first_name":results[0]["first_name"],
            "last_name":results[0]["last_name"],
            "email":results[0]["email"],
            "password":results[0]["password"],
            "created_at":results[0]["users.created_at"],
            "updated_at":results[0]["users.updated_at"]
            }
        one_recipe.user=(user.User(user_data))
        print("one_recipe", one_recipe)
        return one_recipe
    @classmethod
    def update_info(cls,data):
        query="""
        UPDATE recipes
        SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, date=%(date)s, time=%(time)s, updated_at=NOW()
        WHERE id=%(id)s"""
        results=connectToMySQL('recipes').query_db(query,data)
        print("results", results)
        return results
    @classmethod
    def delete_info(cls,data):
        query="""
        DELETE 
        FROM recipes
        WHERE id=%(id)s
        ;"""
        results=connectToMySQL('recipes').query_db(query,data)
        return results