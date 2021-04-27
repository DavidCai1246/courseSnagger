from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title='Home')

@app.route("/about")
def about():
	return render_template("about.html", title='About')

@app.route("/snag")
def snag():
	return render_template("snag.html", title='Snag')

if __name__ == '__main__':
	app.run(debug=True)