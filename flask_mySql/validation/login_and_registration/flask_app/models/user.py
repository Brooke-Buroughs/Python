from flask_app.config.mysqlconnection import connectToMySQL
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
    @classmethod
    def save(cls,data):
        query="INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('login_and_registration').query_db(query,data)
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
    def get_one(cls, data):
        query="""
        SELECT * 
        FROM users 
        WHERE users.id=%(user_id)s
        ;"""
        results=connectToMySQL('login_and_registration').query_db(query,data)
        user1=cls(results[0])
        for user0 in results:
            data={
                "id":user0['id'],
                "first_name":user0['first_name'],
                "last_name":user0['last_name'],
                "email":user0['email'],
                "password":user0['password']
            }
        print(user1)
        return user1
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_and_registration").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])