import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    id = session["user_id"]
    stocks = db.execute("SELECT * FROM stocks WHERE id=:id", id=id)
    cashlist = db.execute("SELECT cash FROM users WHERE id=:id", id=id)
    totalcash = 0
    for cash in cashlist:
        cash = cash['cash']
    for diffstocks in stocks:
        diffstocks['price'] = usd(lookup(diffstocks['symbol'])['price'])
        totalcash += (lookup(diffstocks['symbol'])['price'] * diffstocks['amount'])
    totalcash += cash
    for diffstocks in stocks:
        diffstocks['total'] = usd(lookup(diffstocks['symbol'])['price'] * diffstocks['amount'])
        db.execute("UPDATE stocks SET total = :total WHERE id = :id AND symbol = :symbol", total=diffstocks['total'], id=id, symbol=diffstocks['symbol'])
    return render_template("index.html", stocks=stocks, cash=usd(cash), totalcash=usd(totalcash))
    


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    
    if request.method == "POST":
            
        ids = session["user_id"]
        symbol = lookup(request.form.get("symbol"))['symbol']
        amount = int(request.form.get("shares"))
        price = lookup(symbol)['price']
        name = lookup(symbol)['name']
        
        if amount < 1:
            return apology("Invalid amount of shares", 403)
                
        if not lookup(symbol):
            return apology("Could not find the stock", 403)
        
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=ids)[0]['cash']
        
        cash_after = cash - price * amount

        if cash_after < 0:
            return apology("Not enough money", 403)
          
        stock = db.execute("SELECT amount FROM stocks WHERE id = :id AND symbol = :symbol", 
             id=ids, symbol=symbol)
             
        if not stock:
           db.execute("INSERT INTO stocks (id, symbol, name, price, amount, total) VALUES (:id, :symbol, :name, :price, :amount, :total)", 
                id=ids, symbol=symbol, name=name, price=usd(price), amount=amount, total=usd(amount * price))
           db.execute("INSERT INTO histories (id, symbol, name, price, amount) VALUES (:id, :symbol, :name, :price, :amount)",
                id=ids, symbol=symbol, name=name, price=usd(price), amount=amount)
        else:
            db.execute("INSERT INTO histories (id, symbol, name, price, amount) VALUES (:id, :symbol, :name, :price, :amount)",
                id=ids, symbol=symbol, name=name, price=usd(price), amount=amount)
            amount += stock[0]['amount']
            db.execute("UPDATE stocks SET amount = :amount WHERE id = :id and symbol = :symbol", amount=amount,
                id=ids, symbol=symbol)

                
        db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=cash_after, id=ids)
        
        flash("Bought!")
        return redirect("/")
    else:
        return render_template("buy.html")
        
@app.route("/history")
@login_required
def history():
        stocks = db.execute("SELECT * from histories WHERE id = :id", id=session['user_id'])
        return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for usernameg
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    if request.method == "POST":
        deposit = int(request.form.get("deposit"))
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session['user_id'])
        after_cash = deposit + cash[0]['cash']
        db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=after_cash, id=session['user_id'])
        flash("Deposited!")
        return redirect("/")
    else:
        return render_template("deposit.html")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    
    if request.method == "POST":
        stock = lookup(request.form.get("symbol"))
        
        if not stock:
            return apology("Could not find stock", 403)
        else:
            return render_template("quoted.html", stock=stock)
        
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        
        # Ensure password confirmation was sumbitted    
        elif not request.form.get("passwordcheck"):
            return apology("must provide the same password", 403)
        
        # Ensure password is the same as the password confirmation    
        elif request.form.get("password") != request.form.get("passwordcheck"):
            return apology("passwords don't match", 403)

        # Query 
        elif db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username")):
            return apology("username is already taken", 403)

        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

        rows = db.execute("SELECT * FROM users WHERE username = :username", usename=reqest.form.get("username"))
        
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return render_template("login.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    
    #If submitting the form
    if request.method == "POST":
        
        #Select the number of stocks the selected symbol
        stock = db.execute("SELECT amount from stocks WHERE id = :id and symbol = :symbol", id=session["user_id"],  symbol=request.form.get("symbol"))
        
        #Select the amount of cash the user has
        cash = db.execute("SELECT cash from users WHERE id = :id", id=session['user_id'])
        for money in cash:
            cash = int(money['cash'])
        
        #If the stock isnt there return an apology
        if not stock:
            return apology("stocks not found, 403")
        #If the stock is there
        else:
            for amount in stock:
                
                #If the amount of stocks avalible is more than being sold
                if int(amount['amount']) > int(request.form.get("shares")):
                    
                    #Amount of shares avalible - amount of shares sold
                    new_amount = (int(amount['amount']) - int(request.form.get("shares")))
                    
                    #New Stock Price of the symbol
                    stockprice = lookup(request.form.get('symbol'))['price']
                    
                    #Update the amount of stocks avalible to the new amount
                    db.execute("UPDATE stocks SET amount = :amount WHERE id = :id AND symbol = :symbol", amount=new_amount, id=session['user_id'], symbol=request.form.get("symbol"))
                    
                    #Update the amount of cash to the stock price multipled by the amount of stocks sold and adding the remaining stocks
                    db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=(cash + stockprice * int(request.form.get("shares"))), id=session['user_id'])
                    
                    #Input this transaction into history
                    db.execute("INSERT INTO histories (id, symbol, name, price, amount) VALUES (:id, :symbol, :name, :price, :amount)",
                    id=session['user_id'], symbol=request.form.get("symbol"), name=lookup(request.form.get("symbol"))['name'], price=usd(stockprice), amount=(int(request.form.get("shares")) * -1))
                    
                    #The amount of stocks avalible is equal to the amount being sold
                elif int(amount['amount']) == int(request.form.get("shares")):
                    
                    #Amount of shares avalible - amount of shares sold
                    new_amount = (int(amount['amount']) - int(request.form.get("shares")))
                    
                    #New Stock Price of the symbol
                    stockprice = lookup(request.form.get('symbol'))['price']
                    
                    #Update the amount of stocks avalible to the new amount
                    db.execute("UPDATE stocks SET amount = :amount WHERE id = :id AND symbol = :symbol", amount=new_amount, id=session['user_id'], symbol=request.form.get("symbol"))
                    
                    #Update the amount of cash to the stock price multipled by the amount of stocks sold and adding the remaining stocks
                    db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash=(cash + stockprice * int(request.form.get("shares"))), id=session['user_id'])
                   
                    #Delete the stocks that was selected since it has cancelled out
                    db.execute("DELETE FROM stocks WHERE id = :id AND symbol = :symbol", id=session['user_id'], symbol=request.form.get("symbol"))
               
                    #Input this transaction into history
                    db.execute("INSERT INTO histories (id, symbol, name, price, amount) VALUES (:id, :symbol, :name, :price, :amount)",
                    id=session['user_id'], symbol=request.form.get("symbol"), name=lookup(request.form.get("symbol"))['name'], price=usd(stockprice), amount=(int(request.form.get("shares")) * -1))
                #If the amount of stocks is less than the amount being sold
                else:
                    return apology("insufficient amount of shares", 403)
            
            flash("Sold")
            return redirect("/")
    else:
        stockselection = db.execute("SELECT symbol from STOCKS where id = :id", id=session["user_id"])
        return render_template("sell.html", stockselection=stockselection)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
