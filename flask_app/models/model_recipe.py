from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash


class Recipe:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.under_thirty=data['under_thirty']
        self.made_on=data['made_on']
        self.user_id=data['user_id']
        self.created_at=data['created_at']
        self.created_at=data['updated_at']


    # C
    @classmethod
    def create(cls, data:dict) -> int:
        query="INSERT INTO recipes (name, description, instructions, under_thirty, made_on, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_thirty)s, %(made_on)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R
    @classmethod
    def get_one(cls, data:dict) -> list:
        query="SELECT * FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query="SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipes = []
            for recipe in results:
                all_recipes.append(cls(recipe))
            return all_recipes
        return False

    # U
    @classmethod
    def update_one(cls, data:dict) -> None:
        query="UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_thirty=%(under_thirty)s, made_on=%(made_on)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # D
    @classmethod
    def delete_one(cls, data:dict) -> None:
        query="DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    
    @staticmethod
    def validate_recipe(data):
        is_valid=True

        # Check Name Field
        if not data['name'] or len(data['name']) < 2:
            flash("Please enter a name for your recipe.", "err_name")
            is_valid=False
        
        # Check Description Field
        if not data['description'] or len(data['description']) < 2:
            flash("Please provide a desription for your recipe.", "err_description")
            is_valid = False
        
        # Check Instructions Field
        if not data['instructions'] or len(data['instructions']) < 2:
            flash("Please provide instructions for your recipe.", "err_instructions")
            is_valid=False
        
        # Check Date Field
        if not data['made_on']:
            flash("When did you make this recipe?", "err_made_on")
            is_valid=False
        
        # Check Under 30 Field
        if 'under_thirty' not in data:
            flash("Please choose an option.", "err_under_thirty")
            is_valid=False
        
        return is_valid