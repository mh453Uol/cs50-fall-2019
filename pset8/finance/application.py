import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from persistence import *

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

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # 1. Get user cash
    # 2. Get user purchases

    user_id = session["user_id"]

    rows = get_user_cash(user_id)

    if len(rows) != 1:
        return apology("Could not find user", len(rows))

    user_cash = rows[0]["cash"]

    rows = get_remaining_shares(user_id)
    purchases = rows
    grand_total = user_cash

    print(purchases)

    for purchase in purchases:
        share = lookup(purchase["purchased_symbol"])

        if share:
            purchase["name"] = share["name"]
            purchase["current_share_price"] = share["price"]
            purchase["total_current_price"] = purchase["current_share_price"] * purchase["remaining_shares"]
            purchase["total_price"] = purchase["remaining_shares"] * purchase["purchased_share_price"]
            purchase["profit"] = purchase["total_current_price"] - purchase["total_price"]

        grand_total = grand_total + purchase["total_current_price"]

    model = {
        'purchases': purchases,
        'user_cash': user_cash,
        'grand_total': grand_total
    }

    #print(model)

    return render_template("index.html", model=model)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":

        # buying stock with n numbers of shares
        # 1. Find stock price
        # 2. Total Price = stock price * shares
        #   2.1 If you has funds
        #       2.1.1 Create purchase records
        #       2.1.2 Update To total
        #   2.1 If NOT has funds
        #       2.1.1 return appology

        symbol = request.form.get("symbol")
        share = int(request.form.get("share"))

        if not symbol or not share:
            return apology(f"please provide both symbol and shares", 403)

        if share <= 0:
            return apology(f"shares need to be more than 0", 403)

        stock = lookup(symbol)

        if stock is None:
            return apology(f"{symbol} symbol does not exist", 404)

        stock_price = stock["price"]
        total_price = stock_price * share
        user_id = session["user_id"]

        rows = get_user_cash(user_id)

        if len(rows) != 1:
            return apology("user does not exist",404)

        user_cash = float(rows[0]["cash"])

        if total_price > user_cash:
            return apology("you cannot afford the number of shares at the current price")
        else:
            # has funds so create purchase records
            buy_shares(symbol,stock_price, share, user_id)

            user_cash = user_cash - total_price

            update_user_cash(user_cash, user_id)

            return redirect(url_for("index"))
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    username = request.args.get("username")

    if not username:
        return jsonify(False)

    exists = get_user_by_username(username);

    if len(exists) == 0:
        return jsonify(True)

    return jsonify(False)


@app.route("/history")
@login_required
def history():

    """Show history of transactions"""

    user_id = session["user_id"]

    data = see_all_purchases_and_sold_shares(user_id)

    model = {
        'transactions': data
    }

    return render_template("history.html",model=model)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 401)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 402)

        # Query database for username
        rows = get_user_by_username(username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", len(rows))

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        data = lookup(symbol)

        if data is None:
            return apology(f"{symbol} symbol does not exist", 400)
        else:
            return render_template("quoted.html",model=data)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must provide username", 400)

        if not password:
            return apology("must provide password", 400)

        if not confirmation:
            return apology("must provide confirm password", 400)

        if not confirmation == password:
            return apology("confirm password & password must match", 400)

        # check username doesnt exists
        rows = get_user_by_username(username)

        if len(rows) != 0:
            return apology("username already exists", 400)

        # if we reached this far user doesnt exists so add them
        hashed_password = generate_password_hash(password)
        user_id = add_user(username, hashed_password)

        return redirect("/login")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # 1. Get user shares
    #   1.1 Find each purchased symbol - shares
    #   1.2 Find each sold symbol - shares
    #   1.3 purchases - sold = remaining
    user_id = session["user_id"]

    if request.method == "POST":

        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        rows = get_remaining_shares_for_stock(symbol, user_id)

        #print(rows)

        if len(rows) != 1:
            return apology(f"You dont own any shares for ${symbol}")
        else:
            remaining_shares = rows[0]["remaining_shares"]

            if shares > remaining_shares:
                return apology(f"you only have ${remaining_shares} shares in ${symbol}")
            else:
                user_rows = get_user_cash(user_id)

                if len(user_rows) != 1:
                    return apology("User doesnt exist")

                user_cash = float(user_rows[0]["cash"])
                share_price = lookup(symbol)["price"]
                total_share_price = shares * share_price
                new_user_cash = user_cash + total_share_price

                sell_shares(symbol, shares, user_id, share_price)

                update_user_cash(new_user_cash, user_id)

        return redirect("/")

    else:
        rows = get_remaining_shares(user_id)

        model = {
            'remaining': rows
        }

        #print(model)

        return render_template("sell.html",model=model)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
