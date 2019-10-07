from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    fname = request.form['first_name']
    lname = request.form['last_name']
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    value = int(apple) + int(raspberry) + int(strawberry)
    return render_template("checkout.html", fname = fname, lname = lname, strawberry = strawberry, apple = apple, raspberry = raspberry, value = value)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    