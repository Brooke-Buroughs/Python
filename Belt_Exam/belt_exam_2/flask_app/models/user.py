from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import show
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
        self.shows=[]
    @classmethod
    def save(cls,data):
        query="INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('shows').query_db(query,data)
    @staticmethod
    def validate_user(user):
        email_regex=re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")#parameters for email beginning , after @ & .'com'
        is_valid = True
        if len(user['fname'])<2:
            flash("First name must be at least 4 characters.", 'register')
            is_valid = False
        if len(user['lname'])<2:
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
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("shows").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])
    @classmethod
    def get_one(cls,data):
        # data = {'id' ; id}
        query="""
        SELECT * 
        FROM users 
        LEFT JOIN shows 
        ON users.id=shows.user_id 
        WHERE users.id=%(user_id)s
        ;"""
        results=connectToMySQL('shows').query_db(query,data)
        user1=cls(results[0])
        for show1 in results:
            show_data={
                "id":show1["shows.id"],
                "name":show1["name"],
                "description":show1["description"],
                "network":show1["network"],
                "date":show1["date"],
                "created_at":show1["shows.created_at"],
                "updated_at":show1["shows.updated_at"],
                "user_id":show1["user_id"]
            }
            user1.shows.append(show.Show(show_data))
        print(user1)
        return user1
    @staticmethod
    def validate_input(user):
        is_valid = True
        if len(user['name'])<3:
            flash("Name must be at least 3 characters.", 'show')
            is_valid = False 
        if len(user['description'])<3:
            flash("Description must be at least 3 characters.", 'show')
            is_valid = False
        if len(user['network'])<3:
            flash("Network must be at least 3 characters.", 'show')
            is_valid = False 
        if len (user['date'])<1:
            flash("Please add a date.", 'show')
            is_valid=False
        return is_valid