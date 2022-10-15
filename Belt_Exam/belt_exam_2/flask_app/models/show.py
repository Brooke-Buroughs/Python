from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash 
import re 

class Show:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.network=data['network']
        self.date=data['date']
        self.user_id=data['user_id']
        self.user=None

    @classmethod
    def save(cls,data):
        query="INSERT INTO shows (name, description, network, date, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, %(network)s, %(date)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL('shows').query_db(query,data)
        
    @classmethod
    def get_all(cls):
        query="SELECT * FROM shows JOIN users ON users.id=shows.user_id;"
        results=connectToMySQL('shows').query_db(query)
        shows=[]
        for show1 in results:
            show=cls(show1)
            user_data={
                "id":show1["users.id"],
                "first_name":show1["first_name"],
                "last_name":show1["last_name"],
                "email":show1["email"],
                "password":show1["password"],
                "created_at":show1["users.created_at"],
                "updated_at":show1["users.updated_at"]
            }
            show.user=(user.User(user_data))
            shows.append(show)
        return shows
    @classmethod
    def get_show_by_user(cls, data):
        query="""
        SELECT * 
        FROM shows  
        JOIN users 
        ON users.id=shows.user_id
        WHERE shows.id=%(id)s
        ;"""
        results=connectToMySQL('shows').query_db(query, data)
        print("results",results)
        one_show=cls(results[0])
        user_data={
            "id":results[0]["users.id"],
            "first_name":results[0]["first_name"],
            "last_name":results[0]["last_name"],
            "email":results[0]["email"],
            "password":results[0]["password"],
            "created_at":results[0]["users.created_at"],
            "updated_at":results[0]["users.updated_at"]
            }
        one_show.user=(user.User(user_data))
        print("one_show", one_show)
        return one_show
    @classmethod
    def update_info(cls,data):
        query="""
        UPDATE shows
        SET name=%(name)s, description=%(description)s, network=%(network)s, date=%(date)s, updated_at=NOW()
        WHERE id=%(id)s"""
        results=connectToMySQL('shows').query_db(query,data)
        print("results", results)
        return results
    @classmethod
    def delete_info(cls,data):
        query="""
        DELETE 
        FROM shows
        WHERE id=%(id)s
        ;"""
        results=connectToMySQL('shows').query_db(query,data)
        return results