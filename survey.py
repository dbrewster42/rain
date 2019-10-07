from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def form():
	return render_template('survey.html')

@app.route('/result', methods=['POST'])
def result():
	print("Survey Accepted")
	print(request.form)
	name_from_form = request.form['name']
	want_from_form = request.form['want']
	weapon_from_form = request.form['weapon']
	return render_template('survey2.html', name=name_from_form, want=want_from_form, weapon=weapon_from_form)


if __name__=="__main__":
	app.run(debug=True)