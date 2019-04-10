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
    query = 'SELECT * FROM Pizza WHERE Pizza.name = "{}"'.format(pizza_name)
    cur.execute(query)
    results = cur.fetchall()
    print(results[1])
    return render_template("show_pizza.html", results=results)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
