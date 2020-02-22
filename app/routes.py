from app import app
from flask import render_template
    
@app.route('/')
def index():
    greeting = "We come in peace."
    return render_template('index.html', title='Home', greeting=greeting)

@app.route('/students')
def students():
    greeting = "Welcome to the student spage."
    return render_template('students.html', title='Home', greeting=greeting)

@app.route('/statistics')
def statistics():
    greeting = "Welcome to the statistics page."
    return render_template('statistics.html', title='Home', greeting=greeting)

@app.route('/survey')
def survey():
    greeting = "Welcome to the survey page."
    return render_template('survey.html', title='Home', greeting=greeting)