from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash 
import re

#thought validations and - check how we did this in recipes - 
# like logic 
# save a thought - likes default-
# delete a thought- 
class Thought:
    all_accounts=[]
    def __init__(self,data):
        self.id=data['id']
        self.content=data['content']
        self.likes=data['likes']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        # self.users_id=data['users_id']
        self.user=None
        self.thought_likes=[]
    @classmethod
    def save(cls,data):
        query="INSERT INTO thoughts (users_id, content, likes, created_at, updated_at) VALUES (%(user_id)s, %(content)s, 0, NOW(), NOW());"
        return connectToMySQL('thought_dashboard').query_db(query,data)
    @classmethod
    def delete_info(cls,data):
        query="""
        DELETE 
        FROM thoughts5
        WHERE id=%(id)s
        ;"""
        results=connectToMySQL('thought_dashboard').query_db(query,data)
        return results
    @classmethod
    def get_all(cls):
        query="SELECT * FROM thoughts JOIN users ON users.id=thoughts.users_id;"
        results=connectToMySQL('thought_dashboard').query_db(query)
        thoughts=[]
        for thought1 in results:
            thought=cls(thought1)
            user_data={
                "id":thought1["users.id"],
                "first_name":thought1["first_name"],
                "last_name":thought1["last_name"],
                "email":thought1["email"],
                "password":thought1["password"],
                "created_at":thought1["users.created_at"],
                "updated_at":thought1["users.updated_at"]
            }
            thought.user=(user.User(user_data))
            thoughts.append(thought)
        return thoughts
    @classmethod
    def update(cls, data):
        query="UPDATE thoughts SET users_id=%(user_id)s, likes=%(likes)s, updated_at=NOW() where id=%(id)s;"
        return connectToMySQL('thought_dashboard').query_db(query,data)
    @staticmethod
    def validate_input(thought):
        is_valid = True
        if len(thought['content'])<5:
            flash("Your thought must be at least 5 characters.", 'thought')
            is_valid = False
        return is_valid