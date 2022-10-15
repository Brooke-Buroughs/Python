from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import thought
from flask_app import app
from flask import flash
import re

class User:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.thoughts=[]
    @classmethod
    def save(cls,data):
        query="INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('thought_dashboard').query_db(query,data)
    @staticmethod
    def validate_user(user):
        email_regex=re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")#parameters for email beginning , after @ & .'com'
        is_valid = True
        if len(user['fname'])<4:
            flash("First name must be at least 4 characters.", 'register')
            is_valid = False
        if len(user['lname'])<4:
            flash("Last name must be at least 4 characters.", 'register')
            is_valid = False
        if not email_regex.match(user['email']):
            flash("Invalid email address.", 'register')
            is_valid = False
        if len(user['password'])<15:
            flash("Password must be at least 15 characters.", 'register')
            is_valid = False
        if user['password'] != user['cpass']:
            flash("Password does not match.", 'register')
            is_valid = False
        return is_valid
    @classmethod
    def get_one(cls,data):
        query="""
        SELECT * 
        FROM users 
        LEFT JOIN thoughts 
        ON users.id=thoughts.users_id 
        WHERE users.id=%(id)s
        ;"""
        results=connectToMySQL('thought_dashboard').query_db(query,data)
        user1=cls(results[0])
        for thoughts0 in results:
            thought_data={
                "id":thoughts0["thoughts.id"],
                "content":thoughts0["content"],
                "likes":thoughts0["likes"],
                "created_at":thoughts0["thoughts.created_at"],
                "updated_at":thoughts0["thoughts.updated_at"],
                "user_id":thoughts0["users_id"]
            }
            user1.thoughts.append(thought.Thought(thought_data))
        print(user1)
        return user1
    # @classmethod
    # def get_all(cls,data):
    #     query="SELECT * FROM users JOIN thoughts ON users.id=thoughts.users_id;"
    #     results=connectToMySQL('thought_dashboard').query_db(query,data)
    #     posts=[]
    #     for point in results:
    #         post=cls(point)
    #         post_data={
    #             "id":point['id'],
    #             "content":point['content'],
    #             "likes":data['likes'],
    #             "created_at":data['created_at'],
    #             "updated_at":data['updated_at'],
    #             "user_id":data['user_id']
    #         }
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("thought_dashboard").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])