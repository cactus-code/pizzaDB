from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/show_pizza/<pizza_name>')
def show_pizza(pizza_name):
    #check if pizza_name is valid
    #some db query with pizza_name
    description = "blah blah"
    base = "crispy ofc"
    toppings = ['Tomato', 'Cheese', 'Ham']
    topping_string = ""
    for topping in toppings:
        topping_string += topping + " "
    return render_template("show_pizza.html", name=pizza_name, description
                            =description, base=base, toppings=topping_string)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
