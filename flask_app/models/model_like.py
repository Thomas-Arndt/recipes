from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Like:
    def __init__(self, data):
        self.user_id=data['user_id']
        self.recipe_id=data['recipe_id']
        self.created_at=data['created_at']
        self.created_at=data['updated_at']
        if "first_name" in data:
            self.first_name=data['first_name']
        if "last_name" in data:
            self.last_name=data['last_name']
        if "name" in data:
            self.name=data['name']

    # C
    @classmethod
    def create(cls, data:dict) -> int:
        query="INSERT INTO likes (user_id, recipe_id) VALUES (%(user_id)s, %(recipe_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R
    @classmethod
    def get_one(cls, data:dict) -> list:
        query="SELECT * FROM likes WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query="SELECT * FROM likes;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_likes = []
            for like in results:
                all_likes.append(cls(like))
            return all_likes
        return False

    @classmethod
    def get_all_likes_by_recipe(cls, data:dict) -> list:
        query="SELECT * FROM users RIGHT JOIN likes ON user_id=users.id WHERE likes.recipe_id = %(recipe_id)s;"
        results=connectToMySQL(DATABASE).query_db(query, data)
        if results:
            all_likes = []
            for like in results:
                all_likes.append(cls(like))
            return all_likes
        return False

    @classmethod
    def get_likes_by_recipe_and_user(cls, data:dict) -> list:
        query="SELECT * FROM users RIGHT JOIN likes ON user_id=users.id WHERE likes.recipe_id = %(recipe_id)s AND likes.user_id = %(user_id)s;"
        results=connectToMySQL(DATABASE).query_db(query, data)
        if results:
            all_likes = []
            for like in results:
                all_likes.append(cls(like))
            return all_likes
        return False

    @classmethod
    def get_all_likes_by_user(cls, data:dict) -> list:
        query="SELECT * FROM recipes RIGHT JOIN likes ON recipe_id=recipes.id WHERE likes.user_id = %(user_id)s;"
        results=connectToMySQL(DATABASE).query_db(query, data)
        if results:
            all_likes = []
            for like in results:
                all_likes.append(cls(like))
            return all_likes
        return False

    # U
    @classmethod
    def update_one(cls, data:dict) -> None:
        query="UPDATE likes SET user_id=%(user_id)s, recipe_id=%(recipe_id)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # D
    @classmethod
    def delete_one(cls, data:dict) -> None:
        query="DELETE FROM likes WHERE user_id=%(user_id)s AND recipe_id=%(recipe_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete_all_by_recipe(cls, data:dict) -> None:
        query="DELETE FROM likes WHERE recipe_id=%(recipe_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)