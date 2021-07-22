# ------------- Imports

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from functools import wraps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# ------------- Flask App Configuration

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Credit:
# https://github.com/TravelTimN/flask-task-manager-project/blob/demo/app.py
# https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # no "user" in session
        if "user" not in session:
            flash("You must log in to view this page")
            return redirect(url_for("login"))
        # user is in session
        return f(*args, **kwargs)
    return decorated_function


# ------------------ Home


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# ------------------- Recipes


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())

    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# ------------------- Register

# Credit:
# https://github.com/TravelTimN/flask-task-manager-project/blob/demo/app.py


@app.route("/register", methods=["GET", "POST"])
def register():
    if "user" not in session:
        # only if there isn't a current session["user"]
        if request.method == "POST":
            # check if user already exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username alreay exists")
                return redirect(url_for("register"))

            register = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("email_address").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
                "is_admin": False
            }
            mongo.db.users.insert_one(register)

            # put user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Welcome, {} ! Let's start creating!".format(
                request.form.get("username")))
            return redirect(url_for("profile", username=session["user"]))

        return render_template("register.html")

    # User is already logged-in, direct them to their profile
    return redirect(url_for("profile", username=session["user"]))

# ------------------------- Login


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" not in session:
        # only if there isn't current session["user"]
        if request.method == "POST":
            # check if username exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                # ensure hashed password matches user input
                if check_password_hash(
                    existing_user['password'], request.form.get(
                        "password")):
                    session["user"] = request.form.get("username").lower()
                    user = mongo.db.users.find_one(
                        {"username": session["user"]})
                    # check if user is admin
                    if user["is_admin"]:
                        session["is_admin"] = True
                    else:
                        session["is_admin"] = False
                    flash("Welcome back {} ! Let's start creating!".format(
                            request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
                else:
                    # invalid password match
                    flash(
                        "Incorrect Username and/or Password, please try again")
                    return redirect(url_for("login"))

            else:
                # username doesn't exist
                flash("Incorrect Username and/or Password, please try again")
                return redirect(url_for("login"))

        return render_template("login.html")

    # user is already logged-in, direct them to their profile
    return redirect(url_for("profile", username=session["user"]))


# --------------------- Profile


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    # grab the session user's username form db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find(
        {"created_by": session["user"]}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


# ---------------- Logout


@app.route("/logout")
@login_required
def logout():
    # remove user form session cookies
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# ------------ Add Recipe


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "recipe_url": request.form.get("recipe_url"),
            "category": request.form.get("category_name"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "prep_time": request.form.get("prep_time"),
            "serves": request.form.get("serves"),
            "created_by": session["user"]
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added!")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("name", 1)

    return render_template("add_recipe.html", categories=categories)


# ------------------- Edit Recipe


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    """
    User can edit their recipe
    """
    if request.method == "POST":
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {
            "$set": {
                    "recipe_name": request.form.get("recipe_name"),
                    "image_url": request.form.get("image_url"),
                    "recipe_url": request.form.get("recipe_url"),
                    "category": request.form.get("category_name"),
                    "ingredients": request.form.getlist("ingredients"),
                    "method": request.form.getlist("method"),
                    "prep_time": request.form.get("prep_time"),
                    "serves": request.form.get("serves"),
                    "created_by": session["user"]
            }})

        flash("Recipe Updated!")
        return redirect(url_for("full_recipe", recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# -------------------- Delete Recipe


@app.route("/delete_recipe/<recipe_id>")
@login_required
def delete_recipe(recipe_id):
    # Allow user to delete their recipe

    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted!")
    return redirect(url_for("profile", username=session["user"]))

# ------------------ Full recipe page


@app.route("/full_recipe/<recipe_id>")
@login_required
def full_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("full_recipe.html", recipe=recipe)


# ------------ Categories


@app.route("/get_categories")
@login_required
def get_categories():

    if "user" in session:
        user = mongo.db.users.find_one({"username": session["user"]})
        if user["is_admin"]:
            categories = list(
                mongo.db.categories.find().sort("category_name", 1))
            return render_template(
                "get_categories.html", categories=categories, user=user)
        else:
            flash("You do not have permission to view this page")
            return redirect(url_for("profile", username=session["user"]))


# ------------ Add Category
# Inspired by:
# https://github.com/DonnaIB/surround_yourself_with_spanish/blob/master/app.py

@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    # check if user is in session
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        # check if user is admin
        if user["is_admin"]:
            existing_category = mongo.db.categories.find_one(
                {"category_name": request.form.get(
                    "category_name")})
            # check if category exists
            if existing_category:
                flash("Category already exists")
            elif request.method == "POST":
                category = {
                    "category_name": request.form.get("category_name")
                }

                mongo.db.categories.insert_one(category)
                flash("New category has been added!")
                return redirect(url_for("get_categories"))

        return render_template("add_category.html")
    else:
        flash("You do not have permission to view this page")
        return redirect(url_for("profile", username=session["user"]))


# --------- Newsletter Subscribtion
# Inspired from:
# https://github.com/juanstelling/MS3_breaktasty/blob/fe5b544beb648f153f69f362bf06b31bcc3e7b09/app.py

@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        # check for existing email
        existing_email = mongo.db.subscribers.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("You already have a subcribtion!")
            return redirect('home')
        subscriber = {
            "email": request.form.get("email").lower()
        }
        mongo.db.subscribers.insert_one(subscriber)

    flash("Thank you for subscribing!")
    return redirect(url_for('home'))


# ---------- Run app


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
