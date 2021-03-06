from flask import Flask, render_template, flash
from forms import SignUpForm
from helper.snag import snagCourse
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title='Home')

@app.route("/about")
def about():
	return render_template("about.html", title='About')

@app.route("/snag", methods=['GET', 'POST'])
def snag():
	form = SignUpForm()
	if form.validate_on_submit():
		flash(f'Success', 'success')
		result = snagCourse(form.CourseName.data, form.CourseNumber.data, form.CourseSection.data, form.email.data)
	return render_template("snag.html", title='Snag', form=form)

if __name__ == '__main__':
	app.run(debug=True)