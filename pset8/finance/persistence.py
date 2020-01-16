from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

def get_remaining_shares(user_id):
    return db.execute("""
    SELECT purchased_symbol, coalesce(purchased_shares,0) - coalesce(sold_shares,0) as remaining_shares, purchased_share_price
        FROM
            (SELECT symbol as purchased_symbol, SUM(shares) as purchased_shares, share_price as purchased_share_price
                FROM purchases
                WHERE user_id = :user_id
                GROUP BY symbol)
        LEFT OUTER JOIN
            (SELECT symbol as sold_symbol, SUM(shares) as sold_shares
                FROM sold
                WHERE user_id = :user_id
                GROUP BY symbol)
        ON purchased_symbol = sold_symbol
        WHERE remaining_shares > 0""",user_id = user_id)

def get_remaining_shares_for_stock(symbol, user_id):
    return db.execute("""
        SELECT purchased_symbol, coalesce(purchased_shares,0) - coalesce(sold_shares,0) as remaining_shares
            FROM
                (SELECT symbol as purchased_symbol, SUM(shares) as purchased_shares
                    FROM purchases
                    WHERE user_id = :user_id AND symbol = :symbol
                    GROUP BY symbol)
            LEFT OUTER JOIN
                (SELECT symbol as sold_symbol, SUM(shares) as sold_shares
                    FROM sold
                    WHERE user_id = :user_id AND symbol = :symbol
                    GROUP BY symbol)
            ON purchased_symbol = sold_symbol
            WHERE remaining_shares > 0""", symbol=symbol, user_id=user_id)

def get_user_cash(user_id):
    return db.execute("SELECT cash FROM users WHERE id = :user_id", user_id = user_id)

def get_user_by_username(username):
    return db.execute("SELECT * FROM users WHERE username = :username1",username1=username)

def add_user(username, hashed):
    return db.execute("INSERT INTO users ('username', 'hash') VALUES (:username, :hashed)",
            username=username, hashed=hashed)

def buy_shares(symbol, share_price, shares, user_id):
    return db.execute("""INSERT INTO purchases ('symbol','share_price','shares','user_id')
                        VALUES (:symbol, :stock_price, :shares, :user_id)""",
                        symbol=symbol, stock_price=share_price,shares=shares, user_id=user_id)

def sell_shares(symbol, shares, user_id, share_price):
    return db.execute("""INSERT INTO sold ('symbol', 'shares', 'user_id', 'share_price')
                    VALUES (:symbol, :shares, :user_id, :share_price)""",
                    symbol=symbol, shares=shares, user_id=user_id, share_price=share_price)

def update_user_cash(user_cash, user_id):
    return db.execute("""UPDATE users SET cash = :cash WHERE id = :user_id""", cash=user_cash, user_id=user_id)

def see_all_purchases_and_sold_shares(user_id):
    return db.execute("""
        SELECT id, symbol, share_price, shares, created, user_id, 1 as is_purchase
            FROM purchases
            WHERE user_id = :user_id
        UNION ALL
        SELECT id, symbol, share_price, shares, created, user_id, 0 as is_purchase
            FROM sold
            WHERE user_id = :user_id
        ORDER BY created DESC""",user_id=user_id)

