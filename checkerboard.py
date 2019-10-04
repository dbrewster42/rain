from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
	return render_template('checker.html', num=int(4), num2=int(4), col = "red", col2 = "black")

@app.route('/<number>')
def custom(number):
	number = int(number)/2
	return render_template('checker.html', num = int(number), num2=int(4), col = "red", col2 = "black")

@app.route('/<number>/<number2>')
def custom2(number, number2):
	number = int(number)/2
	number2 = int(number2)/2
	return render_template('checker.html', num = int(number), num2 = int(number2), col = "red", col2 = "black")

@app.route('/<number>/<number2>/<color>/<color2>')
def custom3(number, number2, color, color2):
	number = int(number)/2
	number2 = int(number2)/2
	return render_template('checker.html', num = int(number), num2 = int(number2), col = color, col2 = color2)

if __name__=="__main__":
	app.run(debug=True)