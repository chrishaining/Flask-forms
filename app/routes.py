from app import app
from flask import render_template, request, redirect
from forms import NewStudentForm

app.config['SECRET_KEY'] = 'randomtext'

@app.route('/')
def index():
    greeting = "We come in peace."
    return render_template('index.html', title='Home', greeting=greeting)

@app.route('/students')
def students():
    greeting = "Welcome to the student spage."
    return render_template('students.html', title='Home', greeting=greeting)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = NewStudentForm()
    if form.is_submitted():
        result = request.form
        return render_template('success.html', result=result)
    return render_template('add_student.html', form=form)

@app.route('/statistics')
def statistics():
    greeting = "Welcome to the statistics page."
    return render_template('statistics.html', title='Home', greeting=greeting)

@app.route('/survey')
def survey():
    greeting = "Welcome to the survey page."
    return render_template('survey.html', title='Home', greeting=greeting)