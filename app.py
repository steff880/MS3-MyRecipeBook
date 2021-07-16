# ------------- Imports

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
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

# ------------------ Home


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

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
                flash("Welcome back {} ! Let's start creating!".format(
                        request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password, please try again")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password, please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


# --------------------- Profile


@app.route("/profile<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username form db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    recipes = list(mongo.db.recipes.find(
        {"created_by": ObjectId(user["_id"])}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


# ---------------- Logout


@app.route("/logout")
def logout():
    # remove user form session cookies
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# ------------ Add Recipe


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "recipe_url": request.form.get("recipe_url"),
            "category": request.form.get("category_name"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "prep_time": request.form.get("prep_time"),
            "serves": request.form.get("serves"),
            "created_by": ObjectId(user["_id"])
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added!")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("name", 1)

    return render_template("add_recipe.html", categories=categories)

# ---------- Run app


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
