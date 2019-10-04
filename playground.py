from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def boxes():
	return render_template('play2.html', num=int(3), col="blue")

@app.route('/play/<number>/<color>')
def pick(number, color):
	return render_template('play2.html', num=int(number), col=color)

if __name__=="__main__":
	app.run(debug=True)