from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.model_like import Like

# @app.route('/likes/new')
# def likes_new():
#     return render_template("likes_new.html")

@app.route('/likes/create/<int:user_id>/<int:recipe_id>')
def likes_create(user_id, recipe_id):
    if not "uuid" in session:
        return redirect('/')
    data = {
        "user_id": user_id,
        "recipe_id": recipe_id
    }
    like = Like.create(data)
    return redirect('/recipes/'+str(recipe_id))

# @app.route('/likes/<int:id>')
# def likes_show(id):
#     return render_template("likes_show.html")

# @app.route('/likes/<int:id>/edit')
# def likes_edit(id):
#     return render_template("likes_edit.html")

# @app.route('/likes/<int:id>/update', methods=['POST'])
# def likes_update(id):
#     return redirect('/')

@app.route('/likes/delete/<int:user_id>/<int:recipe_id>/<int:referrer>')
def likes_delete(user_id, recipe_id, referrer):
    if not "uuid" in session:
        return redirect('/')
    data = {
        "user_id": user_id,
        "recipe_id": recipe_id
    }
    print(user_id)
    print(recipe_id)
    Like.delete_one(data)
    if referrer == 1:
        return redirect('/recipes/'+str(recipe_id))
    else:
        return redirect('/users/show')