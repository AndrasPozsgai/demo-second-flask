from flask import Flask, render_template, url_for, redirect,request
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/')
def home():
	return ("Hello world")

@app.route('/welcome/')
def welcome():
	return render_template("welcome.html")

@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method =='POST':
		if reqest.form['username'] != 'admin' or request.form['passworld']!= 'admin':
			error = 'Érvénytelen szövegbevitel, próbáld újra'
		else: 
			return redirect(url_for('home'))
	return der_template(url_for('login.html'error=error))



if __name__ == '__main__':
	app.run(debug=True)
