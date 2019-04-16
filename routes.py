from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/pizzas')
def pizzas():
    conn = sqlite3.connect('db/pizzas.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Pizza")
    results = cur.fetchall()
    return render_template("pizzas.html", results=results)


@app.route('/pizza/<pizza_name>')
def pizza(pizza_name):
    conn = sqlite3.connect('db/pizzas.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Pizza WHERE Pizza.name = ?", (pizza_name,))
    pizza_results = cur.fetchone()
    cur.execute("SELECT * FROM Base WHERE Base.id =?", (pizza_results[3],))
    base = cur.fetchone()
    cur.execute('''SELECT Topping.name as Topping, Topping.description as
    Description FROM Pizza, Topping, PizzaTopping WHERE Pizza.name =
    "{}" AND Pizza.id = PizzaTopping.pid AND Topping.id =
    PizzaTopping.tid'''.format(pizza_name))
    toppings = cur.fetchall()
    toppings_length = len(toppings)
    return render_template("pizza.html", results=pizza_results,
                           base=base[1], toppings=toppings,
                           toppings_length=toppings_length)


@app.route('/toppings')
def toppings():
    conn = sqlite3.connect('db/pizzas.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Topping")
    results = cur.fetchall()
    return render_template("toppings.html", results=results)


@app.route('/topping/<topping_name>')
def topping(topping_name):
    conn = sqlite3.connect('db/pizzas.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Topping WHERE Topping.name = ?",
                (topping_name,))
    topping_results = cur.fetchone()
    return render_template("topping.html", results=topping_results)


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
