import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

#configuration website
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#configuration database
db = SQL("sqlite:///sauceyboys.db")
db.execute("DELETE FROM users")

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        db.execute("INSERT INTO emails (emails) VALUES (:email)", email=email)
        flash("Email Received")
        return redirect("/")
    else:
        cart = db.execute("SELECT * from users WHERE id=:id", id=1)
        if not cart:
            return render_template("home.html",totalcart=0)
        else:
            totalcart = (int(cart[0]['twoyearold']) + int(cart[0]['fiveyearold']) + int(cart[0]['kikkoman']) + int(cart[0]['kikkomantamari']) + int(cart[0]['shiromurasaki']) + int(cart[0]['teriyaki']))
            return render_template("home.html",totalcart=totalcart)
        return render_template("home.html",totalcart=0)
        
@app.route('/faq')
def faq():
    cart = db.execute("SELECT * from users WHERE id=:id", id=1)
    if not cart:
        return render_template("faq.html",totalcart=0)
    else:
        totalcart = (int(cart[0]['twoyearold']) + int(cart[0]['fiveyearold']) + int(cart[0]['kikkoman']) + int(cart[0]['kikkomantamari']) + int(cart[0]['shiromurasaki']) + int(cart[0]['teriyaki']))
        return render_template("faq.html",totalcart=totalcart)
    return render_template("faq.html",totalcart=0)

@app.route('/shop', methods=["GET", "POST"])
def shop():
    if request.method == "POST":
        list = ['twoyearold', 'fiveyearold', 'shiromurasaki', 'kikkoman', 'kikkomantamari', 'teriyaki']
        for sauce in list:
            if not request.form.get("{}".format(sauce)):
                continue
            else:
                quantity = db.execute("SELECT {} from users WHERE id=:id".format(sauce), id=1)
                if not quantity:
                    quantities=int(request.form.get("{}".format(sauce)))
                    db.execute("INSERT into users ({}) VALUES (:quantity)".format(sauce), quantity=quantities)
                else:
                    quantity = db.execute("SELECT {} from users WHERE id=:id".format(sauce), id=1)[0]['{}'.format(sauce)]
                    total = int(quantity) + int(request.form.get("{}".format(sauce)))
                    db.execute("UPDATE users SET {} = :quantity WHERE id=:id".format(sauce), quantity=total, id=1)
                    
        cart = db.execute("SELECT * from users WHERE id=:id", id=1)
        if not cart:
            return render_template("shop.html",totalcart=0)
        else:
            totalcart = (int(cart[0]['twoyearold']) + int(cart[0]['fiveyearold']) + int(cart[0]['kikkoman']) + int(cart[0]['kikkomantamari']) + int(cart[0]['shiromurasaki']) + int(cart[0]['teriyaki']))
            return render_template("shop.html",totalcart=totalcart)
    else:
        return render_template("shop.html",totalcart=0) 
        

@app.route('/cart')
def cart():
    cart = db.execute("SELECT * from users WHERE id=:id", id=1)
    if not cart:
        return render_template("cart2.html",totalcart=0)
    else:
        totalcart = (int(cart[0]['twoyearold']) + int(cart[0]['fiveyearold']) + int(cart[0]['kikkoman']) + int(cart[0]['kikkomantamari']) + int(cart[0]['shiromurasaki']) + int(cart[0]['teriyaki']))
        total = (int(cart[0]['twoyearold']) * 11.98 + int(cart[0]['fiveyearold']) * 19.98 + int(cart[0]['kikkoman']) * 3.99 + int(cart[0]['kikkomantamari']) * 5.99 + int(cart[0]['shiromurasaki']) * 15.98 + int(cart[0]['teriyaki']) * 19.98)
        tax = float(total * 0.07)
        after_tax = total + tax
        return render_template("cart.html",cart=cart, total=total, tax=tax, after_tax=after_tax,totalcart=totalcart)
        
@app.route('/purchase')
def purchase():
    db.execute("DELETE FROM users")
    return render_template("purchase.html",totalcart=0)
    